import psycopg2

from db_container import DbContainer
from get_test_data import get_queries_and_cases


test_queries = get_queries_and_cases()


for test_query in test_queries:
    for case in test_query.cases:
        print(f'Setting up a DB for {test_query.name}.{case.name}')
        db = DbContainer()
        try:
            print('Waiting for DB to be ready...')
            db.wait_until_ready()
            print('Connected!')

            with psycopg2.connect(database="postgres",
                                  host="localhost",
                                  user="postgres",
                                  password=db.db_password,
                                  port=db.mapped_port) as conn:

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
            db.stop()
