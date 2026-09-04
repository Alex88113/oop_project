from typing import Annotated, Generator
from datetime import datetime

from pydantic import BaseModel, ValidationError

from classes_and_object.utils.logger import logger

type RESULT_FIND_TASK = Annotated[
    dict[str, str | int | datetime | bool] | None, "Результат найденной задачи"
]

class TaskShame(BaseModel):
    task_id: int
    title: str
    created_at: datetime
    description: str
    status: bool = False

def get_tasks() -> Generator[TaskShame]:
    tasks: list = [
        {
            "task_id": 1,
            "title": "Закончить отчет по продажам",
            "description": "Собрать данные за август, свести таблицы Excel и подготовить презентацию для завтрашнего совещания.",
            "created_at": "2026-09-03T10:30:00",
            "status": False,
        },
        {
            "task_id": 2,
            "title": "Купить продукты на ужин",
            "description": "Список: курица, рис, помидоры, зелень и молоко. Не забыть зайти в магазин на обратном пути с работы.",
            "created_at": "2026-09-03T08:15:00",
            "status": True,
        },
        {
            "task_id": 3,
            "title": "Настроить сервер разработки",
            "description": "Обновить Docker-контейнеры, переустановить зависимости проекта и проверить работу API локально.",
            "created_at": "2026-09-02T18:45:00",
            "status": False,
        },
        {
            "task_id": 4,
            "title": "Позвонить клиенту Иванову",
            "description": "Обсудить условия нового контракта. Контактный телефон: +7-123-456-78-90. Лучшее время для звонка — с 11:00 до 12:00.",
            "created_at": "2026-09-02T09:00:00",
            "status": True,
        },
        {
            "task_id": 5,
            "title": "Написать техническую документацию",
            "description": "Создать описание для модуля авторизации. Формат: Markdown. Готовый файл загрузить в корневую папку проекта.",
            "created_at": "2026-09-01T14:20:00",
            "status": False,
        },
    ]
    try:
        add_tasks = (TaskShame(**task) for task in tasks)
    except ValidationError as error:
        logger.error("При распаковке задач возникла ошибка валидации: {}", error)
        raise
    except Exception as error:
        logger.error("В процессе валидации возникла неизвестная ошибка: {}", error)
        raise

    return add_tasks