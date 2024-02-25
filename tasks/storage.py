from typing import List, Tuple

_DB = []


def add_task(title: str) -> None:
    _DB.append({"title": title, "completed": False})


def remove_task(index: int) -> None:
    _DB.pop(index - 1)


def mark_task_completed(index: int, completed: bool) -> None:
    _DB[index - 1]["completed"] = completed


def get_all_tasks() -> List[Tuple[int, str, bool]]:
    return [("V" if task["completed"] else "-", i + 1, task["title"]) for i, task in enumerate(_DB)]

def check_index(index: int) -> bool:
    if index <= 0:
        print('Enter error: index number can be positive (> 0)')
        return False
    if index > len(_DB):
        print('Enter error: Max index number can be less then all tasks count: ', len(_DB))
        return False
    return True