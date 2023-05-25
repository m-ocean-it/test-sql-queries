import unittest
from typing import List

from deepdiff import DeepDiff

from get_test_data import (FileContentProvider,
                        convert_parsed_paths_to_queries_and_cases)
from models import TestCase, TestQuery


input_data = {
    "query_0":
        {
            "sql_file": "tests/query_0/query.sql",
            "schema_set_up_file": "tests/query_0/setUpSchema.sql",
            "cases": {
                "case_0": {
                    "data_set_up_file": "tests/query_0/case_0/setUpData.sql",
                    "target_set_up_file": "tests/query_0/case_0/setUpTarget.sql"
                },
                "case_1": {
                    "data_set_up_file": "tests/query_0/case_1/setUpData.sql",
                    "target_set_up_file": "tests/query_0/case_1/setUpTarget.sql"
                }
            }
        },
    "query_1":
        {
            "sql_file": "tests/query_1/query.sql",
            "schema_set_up_file": "tests/query_1/setUpSchema.sql",
            "cases": {
                "case_0": {
                    "data_set_up_file": "tests/query_1/case_0/setUpData.sql",
                    "target_set_up_file": "tests/query_1/case_0/setUpTarget.sql"
                },
                "case_1": {
                    "data_set_up_file": "tests/query_1/case_1/setUpData.sql",
                    "target_set_up_file": "tests/query_1/case_1/setUpTarget.sql"
                }
            }
        },
}


class StubFileContentProvider(FileContentProvider):
    data = {"tests/query_0/query.sql": "a",
            "tests/query_0/setUpSchema.sql": "b",
            "tests/query_0/case_0/setUpData.sql": "c",
            "tests/query_0/case_0/setUpTarget.sql": "d",
            "tests/query_0/case_1/setUpData.sql": "e",
            "tests/query_0/case_1/setUpTarget.sql": "f",
            "tests/query_1/query.sql": "g",
            "tests/query_1/setUpSchema.sql": "h",
            "tests/query_1/case_0/setUpData.sql": "i",
            "tests/query_1/case_0/setUpTarget.sql": "j",
            "tests/query_1/case_1/setUpData.sql": "k",
            "tests/query_1/case_1/setUpTarget.sql": "l"}

    def get_file_content(self, path: str):
        return self.data[path]


target: List[TestQuery] = [
    TestQuery(name='query_0', sql='a', schema_set_up_command='b', cases=[
        TestCase(name='case_0', data_set_up_command='c',
                 target_set_up_command='d'),
        TestCase(name='case_1', data_set_up_command='e',
                 target_set_up_command='f')
    ]),
    TestQuery(name='query_1', sql='g', schema_set_up_command='h', cases=[
        TestCase(name='case_0', data_set_up_command='i',
                 target_set_up_command='j'),
        TestCase(name='case_1', data_set_up_command='k',
                 target_set_up_command='l')
    ])
]


class TestGettingQueriesAndCases(unittest.TestCase):
    def test_abc(self):
        result = convert_parsed_paths_to_queries_and_cases(
            input_data, StubFileContentProvider())
        self.assertFalse(DeepDiff(result, target))
