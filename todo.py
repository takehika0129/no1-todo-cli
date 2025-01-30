import argparse
import json
import os

TODO_FILE = "./todos.json"


def load_todos():
    """Load todo items from JSON file if it exists."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            try:
                data = json.load(f)
                return data
            except json.JSONDecodeError:
                return []
    return []


def save_todos(todos):
    """Save todo items to JSON file."""
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f)


def add_item(todos, item):
    """Add an item to the ToDo list."""
    todos.append(item)
    print(f'Added "{item}" to the ToDo list.')
    save_todos(todos)


def list_tasks(todos):
    """List all items in the ToDo list."""
    if not todos:
        print("Your list is empty.")
    else:
        print("Your Todo List:")
        for index, item in enumerate(todos, 1):
            print(f"{index}. {item}")


def remove_item(todos, index):
    """Remove an item from ToDo list by its index (1-based)."""
    try:
        removed_item = todos.pop(index - 1)
        print(f'Removed "{removed_item}" from the ToDo list.')
        save_todos(todos)
    except IndexError:
        print(f"Task with index {index} does not exist. Please provide a valid number between 1 and {len(todos)+1}.")


def main():
    # Load existing todos from file
    todos = load_todos()

    parser = argparse.ArgumentParser(description="Manage a ToDo list.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Sub-commands")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add an item to the ToDo list.")
    parser_add.add_argument("item", help="The item to add.")

    # List command
    parser_list = subparsers.add_parser("list", help="List all items in the ToDo list.")

    # Remove command
    parser_remove = subparsers.add_parser("remove", help="Remove an item from ToDo list by its index (1-based).")
    parser_remove.add_argument("index", type=int, help="Remove an item from the ToDo list.")

    args = parser.parse_args()

    if args.command == "add":
        add_item(todos, args.item)
    elif args.command == "list":
        list_tasks(todos)
    elif args.command == "remove":
        remove_item(todos, args.index)


if __name__ == "__main__":
    main()