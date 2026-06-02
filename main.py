try:
    from task_utils import add_task, mark_completed, view_pending_tasks, get_progress
except ModuleNotFoundError:
    from datetime import datetime

    tasks = []

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
        return [task for task in tasks if not task["completed"]]

    def get_progress():
        total = len(tasks)
        completed = sum(1 for task in tasks if task["completed"])
        pending = total - completed

        if total == 0:
            return {"total": 0, "completed": 0, "pending": 0, "progress": 0.0}

        progress = float((completed / total) * 100)
        return {"total": total, "completed": completed, "pending": pending, "progress": progress}

def main():
    while True:
        print("\nTask Management System")
        print("1. Add task")
        print("2. Mark task as complete")
        print("3. View pending tasks")
        print("4. View progress")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (low/medium/high): ")
            due_date = input("Enter due date (YYYY-MM-DD, optional): ")
            result = add_task(name, priority, due_date)
            if result["success"]:
                print(result["message"])
            else:
                for error in result["errors"]:
                    print(error)
        
        elif choice == "2":
            task_name = input("Enter task name to mark complete: ")
            result = mark_completed(task_name)
            print(result["message"])
        
        elif choice == "3":
            pending = view_pending_tasks()
            if pending:
                for i, task in enumerate(pending, 1):
                    print(f"{i}. {task['name']} - Priority: {task['priority']}")
            else:
                print("No pending tasks")
        
        elif choice == "4":
            progress = get_progress()
            if progress["total"] == 0:
                print("No tasks currently")
            print(f"Total tasks: {progress['total']}")
            print(f"Completed: {progress['completed']}")
            print(f"Pending: {progress['pending']}")
            print(f"Progress: {progress['progress']}%")
        
        elif choice == "5":
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
