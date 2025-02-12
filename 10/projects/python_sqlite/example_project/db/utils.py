import os


def get_script_from_file(filename: str) -> str:
    with open(os.path.join("./example_project", "db", "scripts", filename), "r") as f:
        return f.read()
