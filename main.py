from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    title: str
    description: str

app = FastAPI()

todos: List[Todo] = []

# Creating todos
@app.post('/todos/', response_model=Todo)
async def create_todo(todo: Todo):
    todos.append(todo)
    return todo

# Retrieving all todos
@app.get('/gettodos/', response_model=List[Todo])
async def get_todos():
    return todos

# Retrieve data using Id
@app.get('/gettodos/{id}', response_model=Todo)
def get_todo_by_id(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# updating data using id
@app.put('/gettodos/{id}', response_model=Todo)
def update_todo(id: int, updated_todo: Todo):
    for todo in todos:
        if todo.id == id:
            todo.title = updated_todo.title
            todo.description = updated_todo.description
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# delete data using id
@app.delete('/gettodos/{id}')
def delete_todo_by_id(id: int):
    for i, todo in enumerate(todos):
        if todo.id == id:
            del todos[i]
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")