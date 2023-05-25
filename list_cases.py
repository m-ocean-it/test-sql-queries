import os
from abc import ABC, abstractmethod
from typing import List

from models import TestCase, TestQuery

TESTS_DIRECTORY = 'test_queries'


def run():
    paths = parse_paths_from_os_walk(os.walk(TESTS_DIRECTORY))
    print(paths)


class FileContentProvider(ABC):
    @abstractmethod
    def get_file_content(self, path: str): ...


def convert_parsed_paths_to_queries_and_cases(
        paths: dict,
        file_content_provider: FileContentProvider):

    queries = []
    for query_name, query_data in paths.items():
        q = TestQuery(
            name=query_name,
            sql=file_content_provider.get_file_content(
                query_data['sql_file']),
            schema_set_up_command=file_content_provider.get_file_content(
                query_data['schema_set_up_file']),
            cases=[
                TestCase(
                    name=case_name,
                    data_set_up_command=file_content_provider.get_file_content(
                        case_data['data_set_up_file']),
                    target_set_up_command=file_content_provider.get_file_content(
                        case_data['target_set_up_file']))
                for case_name, case_data
                in query_data['cases'].items()
            ]
        )
        queries.append(q)

    return queries


def parse_paths_from_os_walk(os_walk_output):
    result = {}
    for root, _, files in os_walk_output:
        root_split = root.split(os.path.sep)
        if len(root_split) == 1:
            continue
        if len(root_split) == 2:
            query_name = root_split[1]
            result[query_name] = {'cases': {}}
            for fp in files:
                if fp == 'query.sql':
                    result[query_name]['sql_file'] = os.path.join(
                        root, fp)
                elif fp == 'setUpSchema.sql':
                    result[query_name]['schema_set_up_file'] = os.path.join(
                        root, fp)
        elif len(root_split) == 3:
            query_name = root_split[1]
            case_name = root_split[2]
            result[query_name]['cases'][case_name] = {}
            for fp in files:
                if fp == 'setUpData.sql':
                    result[query_name]['cases'][case_name]['data_set_up_file'] = os.path.join(
                        root, fp)
                elif fp == 'setUpTarget.sql':
                    result[query_name]['cases'][case_name]['target_set_up_file'] = os.path.join(
                        root, fp)
        else:
            raise AssertionError

    return result


if __name__ == '__main__':
    run()
