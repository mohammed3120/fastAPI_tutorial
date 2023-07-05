def indivitual_serial(todo)->dict:
    return{
        "id": str(todo["_id"]),
        "name": str(todo["name"]),
        "description": str(todo["description"]),
        "complete": str(todo["complete"])
    }

def list_serial(todos) -> list:
    return [indivitual_serial(todo) for todo in todos]