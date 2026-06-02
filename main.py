from task_utils import add_task, mark_completed, view_pending_tasks, get_progress

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