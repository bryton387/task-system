try:
    from .validation import validate_task_data
except ImportError:
    import os
    import sys

    sys.path.append(os.path.dirname(__file__))
    from validation import validate_task_data

tasks = []

def add_task(name, priority, due_date=""):
    errors = validate_task_data(name, priority, due_date)
    if errors:
        return {"success": False, "errors": errors}

    clean_due_date = due_date.strip() if isinstance(due_date, str) and due_date.strip() else None

    task = {
        "name": name.strip(),
        "priority": priority.strip(),
        "due_date": clean_due_date,
        "completed": False
    }
    tasks.append(task)
    return {"success": True, "message": "Task added successfully!"}

def mark_completed(task_name):
    if not isinstance(task_name, str):
        return {"success": False, "message": "Task not found"}

    search_name = task_name.strip().lower()
    if search_name.isdigit():
        task_number = int(search_name)
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            return {"success": True, "message": "Task marked as complete!"}

    for task in tasks:
        if task["name"].lower() == search_name:
            task["completed"] = True
            return {"success": True, "message": "Task marked as complete!"}

    return {"success": False, "message": "Task not found"}

def view_pending_tasks():
    pending = [task for task in tasks if not task["completed"]]
    return pending

def calculate_progress(task_list):
    total = len(task_list)
    if total == 0:
        return 0.0

    completed = sum(1 for task in task_list if task.get("completed") == True)
    return float((completed / total) * 100)

def get_progress():
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed

    if total == 0:
        return {"total": 0, "completed": 0, "pending": 0, "progress": 0.0}

    progress = calculate_progress(tasks)
    return {"total": total, "completed": completed, "pending": pending, "progress": progress}
