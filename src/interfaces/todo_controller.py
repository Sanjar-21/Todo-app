from abc import ABC, abstractmethod

class TodoRepository(ABC):
    
    @abstractmethod
    def save(self, todo):
        pass

    @abstractmethod
    def get(self, todo_id):
        pass

    @abstractmethod
    def delete(self, todo_id):
        pass

    @abstractmethod
    def update(self, todo):
        pass