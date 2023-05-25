from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TestCase:
    data_set_up_command: str
    target_set_up_command: str
    name: Optional[str] = None


@dataclass
class TestQuery:
    sql: str
    cases: List[TestCase]
    schema_set_up_command: str
    name: Optional[str] = None
