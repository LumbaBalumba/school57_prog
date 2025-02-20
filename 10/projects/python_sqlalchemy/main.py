from sqlalchemy import or_
from db.models import Task
from db import Session


def main():
    session=Session()
    try:
        while user_input := input():
            args = user_input.split()
            match args[0]:
                case "create" | "cr":
                    name = args[1]
                    desc = " ".join(args[2:])
                    new_task = Task(name=name, description=desc)
                    session.add(new_task)
                    session.commit()

                case "all" | "a":
                    tasks = session.query(Task).all()
                    print(f"Found {len(tasks)} task(s)")
                    for task in tasks:
                        print(
                            f"name: {task.name}, description: '{task.description}', completed: {task.completed}"
                        )
                case "find" | "search" | "f" | "s":
                    pattern = " ".join(args[1:])
                    tasks = session.query(Task).filter(or_(Task.name.contains(pattern), Task.description.contains(pattern))).all()
                    print(f"Found {len(tasks)} task(s)")
                    for task in tasks:
                        print(
                            f"id: {task.id}, name: {task.name}, description: '{task.description}', completed: {task.completed}"
                        )

                case "complete" | "co" | "c":
                    id = int(args[1])
                    task = session.query(Task).filter_by(id=id).one()
                    task.completed = True
                    session.commit()

                case "delete" | "d":
                    id = int(args[1])
                    task = Task.get(id)
                    session.delete(task)
                    session.commit()

                case "quit" | "q" | "exit":
                    break

                case _:
                    raise ValueError("invalid command-line argument")

    except EOFError:
        pass


if __name__ == "__main__":
    main()
