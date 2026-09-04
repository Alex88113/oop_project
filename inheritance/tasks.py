from abc import ABC, abstractmethod
from datetime import datetime
from typing import Annotated, Self

from classes_and_object.utils.logger import logger
from inheritance.shames.task_shame import TaskShame, get_tasks

type RESULT_FIND_TASK = Annotated[
    dict[str, int | str | datetime | bool] | None, "Результат найденной задачи"
]


class Task(ABC):
    def __init__(self) -> None:
        self._tasks: list[TaskShame] = []

    @abstractmethod
    def add_task(self, task: TaskShame) -> Self:
        pass

    @abstractmethod
    def find_by_id(self, task_id: int) -> RESULT_FIND_TASK | None:
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> str | None:
        pass

    @abstractmethod
    def show_all_tasks(self) -> None:
        pass


class TaskManager(Task):
    @staticmethod
    def _validation_task(task: TaskShame) -> TaskShame:
        assert isinstance(task, TaskShame), f"task must be TaskShame, got {type(task).__name__}"
        return task

    def add_task(self, task: TaskShame) -> Self:
        if not isinstance(task, TaskShame):
            raise TypeError("Требуется объект типа TaskShame")

        valid_task = self._validation_task(task)
        self._tasks.append(valid_task)
        return self

    @staticmethod
    def _validation_task_id(task_id: int) -> int:
        assert isinstance(task_id, int), f"task_id must be int, got {type(task_id).__name__}"

        if task_id <= 0:
            logger.error("task_id is negative or equal to zero")
            raise ValueError("task_id is negative or equal to zero")

        return task_id

    def find_by_id(self, task_id: int) -> RESULT_FIND_TASK:
        valid_task_id = self._validation_task_id(task_id)
        for task in self._tasks:
            if task.task_id == valid_task_id:
                return {
                    "task_id": task.task_id,
                    "title": task.title,
                    "description": task.description,
                    "status": task.status,
                    "created_at": task.created_at,
                }

        logger.warning(f"Task with ID: {valid_task_id} not found")
        return None

    def delete_task(self, task_id: int) -> str | None:
        valid_task_id = self._validation_task_id(task_id)

        for index, task in enumerate(self._tasks):
            if task.task_id == valid_task_id:
                self._tasks.pop(index)
                logger.warning(f"The task with ID: {valid_task_id} has been successfully deleted!")
                return f"The task with ID: {valid_task_id} has been successfully deleted!"

        return None

    def show_all_tasks(self) -> None:
        if not self._tasks:
            logger.warning("list with tasks is empty")
            return

        logger.debug("---------------- List all tasks ----------------")
        for task in self._tasks:
            logger.debug(
                f"\nTaskID: {task.task_id}\ntitle: {task.title}\ndescription: {task.description}\nstatus: {task.status}\ncreated_at {task.created_at}"
            )
            logger.debug("-" * 80)
        return


def main() -> None:
    task_manager = TaskManager()
    result_get_tasks = get_tasks()

    for task in result_get_tasks:
        task_manager.add_task(task)
    task_manager.show_all_tasks()


if __name__ == "__main__":
    main()
