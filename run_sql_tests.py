import psycopg2
from termcolor import colored

from db_container import DbContainer
from get_test_data import get_queries_and_cases

queries_to_test = get_queries_and_cases()


for test_query in queries_to_test:
    print('query:', f'"{test_query.name}"')
    for case in test_query.cases:
        print('    case:', f'"{case.name}"', end=' ', flush=True)
        db = DbContainer()
        try:
            db.wait_until_ready()

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

                if result == expected:
                    print(colored('✔', 'green'))
                else:
                    print(colored('✘', 'red'))
        except Exception:
            print(colored('✘', 'red'), '(errored before the test)')
        finally:
            db.stop()
