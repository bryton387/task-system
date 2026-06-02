from datetime import datetime

def validate_task_name(name):
    if not name or len(name.strip()) == 0:
        return False
    return True

def validate_priority(priority):
    valid_priorities = ["low", "medium", "high"]
    if not isinstance(priority, str) or priority.strip().lower() not in valid_priorities:
        return False
    return True

def validate_task_data(name, priority, due_date):
    errors = []
    if not validate_task_name(name):
        errors.append("Task name is required")
    if not validate_priority(priority):
        errors.append("Priority must be low, medium, or high")
    if due_date:
        try:
            datetime.strptime(due_date.strip(), "%Y-%m-%d")
        except ValueError:
            errors.append("Due date must be in YYYY-MM-DD format")
    return errors