def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "description": todo["description"],
        "completed": todo["completed"]
    }

def list_serial(todo) -> list:
    return [individual_serial(todo) for todo in todo]
    