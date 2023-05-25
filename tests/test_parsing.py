from deepdiff import DeepDiff
import unittest
from get_test_data import parse_paths_from_os_walk

input_data = [
    [
        'tests',
        ['query_1', 'query_0'],
        []
    ],
    [
        'tests/query_1',
        ['case_1', 'case_0'],
        ['query.sql', 'setUpSchema.sql']
    ],
    [
        'tests/query_1/case_1',
        [],
        ['setUpData.sql', 'setUpTarget.sql']
    ],
    [
        'tests/query_1/case_0',
        [],
        ['setUpData.sql', 'setUpTarget.sql']
    ],
    [
        'tests/query_0',
        ['case_1', 'case_0'],
        ['query.sql', 'setUpSchema.sql']
    ],
    [
        'tests/query_0/case_1',
        [],
        ['setUpData.sql', 'setUpTarget.sql']
    ],
    [
        'tests/query_0/case_0',
        [],
        ['setUpData.sql', 'setUpTarget.sql']
    ]
]

target = {
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


class TestParsing(unittest.TestCase):
    def test_abc(self):
        self.assertFalse(
            DeepDiff(
                parse_paths_from_os_walk(input_data),
                target))
