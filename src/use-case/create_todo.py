# from Repository.todo_repository import InMemoryTodoRepository



from entities.todo import Todo
from Repository.todo_repository import TodoRepository
class CreateTodo:
    def __init__(self, repo: TodoRepository):
        self.repo = repo
    
    
    def execute(self, title, description):
        if not title:
            raise ValueError("No title")
        
        if not description:
            raise ValueError("No description")

        todo = Todo(title, description)
        self.repo.save(todo)
        return todo