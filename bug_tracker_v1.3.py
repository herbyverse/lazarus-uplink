#Herby Bug Tracker v1.3
# Added Mark as resolved ooption

bugs = []

while True:
    print("\n" + "="*30)
    print("Welcome to Herby's Bug Tracker")
    print("="*30)
    print("1. Report a bug")
    print("2. View all bugs")
    print("3. Exit")
    print("4. Delete a bug")
    print("5. Mark bug as resolved")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        bug = input("Describe the bug: ")
        bugs.append({"description":bug, "resolved": False})
        print("Bug Reported.")
    elif choice == "2":
        print("\nLogged Bugs: ")
        if not bugs:
            print("No bugs yet.")
        else:
            for idx, bug in enumerate(bugs, start=1):
                status = "[x]" if bug["resolved"] else "[]"
                print(f"{idx}. {status} {bug['description']}")
    elif choice == "3":
        print("Goodbye!")
        break
    elif choice == "4":
        if not bugs:
            print("No bugs to delete.")
        else:
            print("Logged Bugs: ")
            for idx, bug in enumerate(bugs, start=1):
                print(f"{idx}. {bug}")
            try:
                delete_index = int(input("Enter the bug number to delete: "))

                if 1 <= delete_index <= len(bugs):
                    removed = bugs.pop(delete_index - 1)
                    print(f"Bug '{removed}' deleted.")
                else:
                    print("Invalid bug number.")
            except ValueError:
                print("Pleasee enter a valid number.")
    elif choice == "5":
        if not bugs:
            print("No bugs to mark as resolved.")
        else:
            for idx, bug in enumerate(bugs, start=1):
                status = "[x]" if bug["resolved"] else "[]"
                print(f"{idx}. {status} {bug['description']}")
            try:
                mark_index = int(input("Enter the number of the bug to mark as resolved: "))
                if 1 <= mark_index <= len(bugs):
                    bugs[mark_index - 1]["resolved"] = True
                    print(f"Bug #{mark_index} marked as resolved.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
          
    else:
        print("Invalid choice. try again.")