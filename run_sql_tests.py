import subprocess
import time
from dataclasses import dataclass
from typing import List, Optional

import psycopg2
import sqlalchemy

from docker_inspect import get_port_of_docker_container
from get_test_data import get_queries_and_cases
from models import TestCase, TestQuery

db_password = "mypassword"

set_up_db = f"docker run -e POSTGRES_PASSWORD={db_password} -p 0:5432 -d --rm postgres"


def check_db_health_cmd(container_id):
    return f"docker exec {container_id} pg_isready -U postgres -d postgres"


def tear_down_db_cmd(container_id) -> str:
    return f"docker stop {container_id}"


test_queries = get_queries_and_cases()


for test_query in test_queries:
    for case in test_query.cases:
        print(f'Setting up a DB for {test_query.name}.{case.name}')

        process_result = subprocess.run(set_up_db.split(),
                                        check=True, capture_output=True)
        container_id = process_result.stdout.decode('utf-8')
        mapped_port = get_port_of_docker_container(container_id)
        try:
            print('Waiting for DB to be ready...')
            healthcheck_count = 0
            while True:
                if healthcheck_count > 20:
                    raise TimeoutError
                print(f'Healthcheck #{healthcheck_count+1}')
                proc = subprocess.run(check_db_health_cmd(container_id).split(),
                                      capture_output=True, check=False)
                if proc.returncode == 0:
                    print("    DB ready!")
                    break
                print('    DB not ready yet')
                healthcheck_count += 1
                time.sleep(1)

            print('Connected!')

            with psycopg2.connect(database="postgres",
                                  host="localhost",
                                  user="postgres",
                                  password=db_password,
                                  port=mapped_port) as conn:

                cursor = conn.cursor()

                commands = [
                    test_query.schema_set_up_command,
                    case.data_set_up_command,
                    case.target_set_up_command
                ]

                for cmd in commands:
                    try:
                        result = cursor.execute(cmd)
                        conn.commit()
                    except Exception as err:
                        print(
                            f"Error '{err}' when executing:\n{cmd}\nContinuing...\n\n")
                        conn.rollback()

                cursor.execute(test_query.sql)
                result = cursor.fetchall()

                queryTargetSql = "SELECT * FROM _test.target"
                cursor.execute(queryTargetSql)
                expected = cursor.fetchall()

                print(result)
                print(expected)
                print(result == expected)
        except Exception:
            print('Errored during testing')
        finally:
            print('Tearing down the DB...')
            subprocess.run(tear_down_db_cmd(container_id).split(),
                           check=True, capture_output=True)
