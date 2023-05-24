from typing import List
from dataclasses import dataclass
import time
import psycopg2
import sqlalchemy
import subprocess

setUpSchemaFilePath = "tests/query_0/setUpSchema.sql"
setUpDataFilePath = "tests/query_0/case_0/setUpData.sql"
setUpTargetFilePath = "tests/query_0/case_0/setUpTarget.sql"
queryFilePath = "tests/query_0/query.sql"

with open(setUpSchemaFilePath, 'r') as f:
    setUpSchemaSql = f.read()
with open(setUpDataFilePath, 'r') as f:
    setUpDataSql = f.read()
with open(setUpTargetFilePath, 'r') as f:
    setUpTargetSql = f.read()
with open(queryFilePath, 'r') as f:
    querySql = f.read()


db_password = "mypassword"
mapped_port = 9999

set_up_db = f"docker run --name test-sql-db -e POSTGRES_PASSWORD={db_password} -p {mapped_port}:5432 -d --rm postgres"
tear_down_db = "docker stop test-sql-db"


@dataclass
class TestCase:
    data_set_up_command: str
    target_set_up_command: str


@dataclass
class TestQuery:
    sql: str
    cases: List[TestCase]
    schema_set_up_command: str


cases = [
    TestCase(data_set_up_command=setUpDataSql,
             target_set_up_command=setUpTargetSql)
]
test_query = TestQuery(sql=querySql, cases=cases, schema_set_up_command=setUpSchemaSql)
test_queries = [test_query]


for test_query in test_queries:
    for i, case in enumerate(cases):
        print(f'Setting up a DB for test case #{i}...')
        subprocess.run(set_up_db.split(), check=True, capture_output=True)
        try:
            sleep_seconds = 4
            print(f'Sleeping for {sleep_seconds} seconds...')
            time.sleep(4)

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
        finally:
            print('Tearing down the DB...')
            subprocess.run(tear_down_db.split(),
                           check=True, capture_output=True)
