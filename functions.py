FILEPATH = r"a.txt"


def get_todo(filepath=FILEPATH):
    """the get_todo() function reads a text file and return list of
        to do items as an output"""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todo(local_todos, filepath=FILEPATH):
    """ Write to do items to the txt file"""
    with open(filepath, "w") as file:
        file.writelines(local_todos)


if __name__ == "__main__":
    print("hello")
    