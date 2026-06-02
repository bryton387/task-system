from datetime import datetime

def validate_task_name(name):
    if not isinstance(name, str) or len(name.strip()) == 0:
        return False
    return True

def validate_priority(priority):
    if not isinstance(priority, str) or len(priority.strip()) == 0:
        return False
    return True

def validate_task_data(name, priority, due_date):
    errors = []
    if not validate_task_name(name):
        errors.append("Task name is required")
    if not validate_priority(priority):
        errors.append("Priority is required")

    if due_date is None:
        due_date = ""

    if due_date:
        if not isinstance(due_date, str):
            errors.append("Due date must be in YYYY-MM-DD format")
            return errors
        try:
            datetime.strptime(due_date.strip(), "%Y-%m-%d")
        except ValueError:
            errors.append("Due date must be in YYYY-MM-DD format")
    return errors
