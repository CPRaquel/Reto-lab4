from fastapi import FastAPI

app = FastAPI()

# Lista de tareas simulada
tasks = [
    {"id": 1, "description": "Hacer la compra", "completed": False},
    {"id": 2, "description": "Pagar las facturas", "completed": False},
    {"id": 5, "description": "Pagar las facturas", "completed": False},
    {"id": 3, "description": "Pagar las facturas", "completed": False}
]

@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi API"}

@app.get("/tasks/")
def lista_tasks():
    return {
        "tasks": tasks
    }
    
@app.get("/tasks/{id}")
def id_tasks(id: str):
    for task in tasks:
        if task.get("id") == int(id):
            return {
                "tasks": task,
            }

    return {
        "message": f"error 404 no existe el id {id}" 
    }        
    
@app.post("/tasks/")
def new_tasks(id: str, description: str):
    for task in tasks:
        if task.get("id") == int(id):
            return {
                "message": f"ya existe el id {id}" 
            }    
    new = {"id": int(id), "description": description, "completed": False}
    tasks.append(new)
    return tasks
    
    
@app.put("/tasks/{id}")
def completed_tasks(id: str):
    for task in tasks:
        if task.get("id") == int(id) and task.get("completed") == False:
            task["completed"] = True
            return {
                "tasks": task
            } 
        elif task.get("id") == int(id):
            task["completed"] = False
            return {
                "tasks": task
            }
    return {
        "message": f"error 404 no existe el id {id}" 
    }           

@app.delete("/tasks/{id}")
def completed_tasks(id: str):
    contador = 0
    for task in tasks:
        if task.get("id") == int(id):
            tasks.pop(contador)
            return {
                "tasks": task
            }
        contador += 1     
    return {
        "message": f"error 404 no existe el id {id}" 
    }     