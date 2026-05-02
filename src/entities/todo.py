import uuid
from datetime import datetime
class Todo:
    def __init__(self, title: str, description: str) -> None:
        """AI is creating summary for __init__

        Args:
            title (str): [description]
            description (str): [description]
        """
        self.title = title
        self.description = description
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.completed = False



def add(a: int, b: int) -> int:
    """AI is creating summary for add

    Args:
        a (int): [description]
        b (int): [description]

    Returns:
        int: [description]
    """
    return a + b