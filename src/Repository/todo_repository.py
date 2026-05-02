import threading
from interfaces.todo_controller import TodoRepository 
from entities.todo import Todo 


class InMemoryTodoRepository(TodoRepository):
    def __init__(self):
        self._storage = {}
        self._lock = threading.Lock()
        
    
    def save(self, todo: Todo):
        with self._lock:
            self._storage[todo.id] = todo

    def get(self, todo_id):
        with self._lock:
            if todo_id in self._storage:
                return self._storage[todo_id]
            else:
                raise ValueError(f"Bunday {todo_id} mavjud emas")

    def delete(self, todo_id):
        with self._lock:
            if todo_id in self._storage:
                del self._storage[todo_id]
            else:
                raise ValueError(f"Bunday {todo_id} mavjud emas")                

    def update(self, todo: Todo):
        with self._lock:
            if todo.id in self._storage:
                self._storage[todo.id] = todo
            else:
                raise ValueError(f"Bunday {todo.id} mavjud emas")