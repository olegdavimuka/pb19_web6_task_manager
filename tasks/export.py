from typing import List, Tuple

from openpyxl import Workbook


def save_to_file(tasks: List[Tuple[int, str, bool]], file_name: str) -> None:
    wb = Workbook()
    ws = wb.active

    ws.append(["Completed", "Index", "Title"])

    for task in tasks:
        ws.append(task)

    wb.save(f"./out/{file_name}.xlsx")
