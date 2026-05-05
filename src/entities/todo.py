import uuid
from datetime import datetime
class Todo:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.completed = False


