import uuid
from dataclasses import dataclass, field, asdict

user_list = []


def get_uuid() -> str:
    return str(uuid.uuid4())


@dataclass(slots=True)
class User:
    first_name: str
    last_name: str
    age: int
    email: str
    children_in_basement: list = field(default_factory=list)
    identification: bool = field(default=True)
    id: str = field(default_factory=get_uuid)

    @property
    def data(self):
        return asdict(self)
