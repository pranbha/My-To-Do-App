FILEPATH = "todos.txt"

def get_todos():
    with open(FILEPATH, "r") as f:
        todos = f.readlines()
    return  todos

def write_todos(todos):
    with open(FILEPATH, "w") as f:
        f.writelines(todos)


if __name__ == "__main__":
    print("Hello")