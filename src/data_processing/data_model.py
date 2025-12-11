from dataclasses import dataclass, fields
from typing import get_type_hints


@dataclass
class EmployeeData:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: str
    team: str
    experience_years: int

    # Автоматическое приведение типов в строке, 
    # т.к. содержание csv считаем валидным.
    def __post_init__(self) -> None:
        type_hints = get_type_hints(type(self))
        for field in fields(self):
            value = getattr(self, field.name)
            expected_type = type_hints[field.name]
            if not isinstance(value, expected_type):
                setattr(self, field.name, expected_type(value))