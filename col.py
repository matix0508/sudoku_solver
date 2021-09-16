from group import Group
from typing import Optional

class Col(Group):
    def __init__(self, id: Optional[int] = None, max_number: Optional[int] = 9) -> None:
        super().__init__(id=id, max_number=max_number)