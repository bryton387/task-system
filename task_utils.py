from validation import validate_task_data

tasks = []

def add_task(name, priority, due_date=""):
    errors = validate_task_data(name, priority, due_date)
    if errors:
        return {"success": False, "errors": errors}
    
    task = {
        "name": name.strip(),
        "priority": priority.lower(),
        "due_date": due_date if due_date else None,
        "completed": False
    }
    tasks.append(task)
    return {"success": True, "message": f"Task '{name.strip()}' added successfully"}

def mark_completed(task_name):
    for task in tasks:
        if task["name"].lower() == task_name.lower():
            task["completed"] = True
            return {"success": True, "message": f"Task '{task_name}' marked as complete"}
    
    return {"success": False, "message": f"Task '{task_name}' not found"}

def view_pending_tasks():
    pending = [task for task in tasks if not task["completed"]]
    return pending

def get_progress():
    total = len(tasks)
    completed = len([task for task in tasks if task["completed"]])
    pending = total - completed
    
    if total == 0:
        return {"total": 0, "completed": 0, "pending": 0, "progress": 0}
    
    progress = (completed / total) * 100
    return {"total": total, "completed": completed, "pending": pending, "progress": round(progress, 2)}