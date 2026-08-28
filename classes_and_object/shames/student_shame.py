from pydantic import BaseModel


class Student(BaseModel):
    student_id: int
    fullname: str
    name: str
    group: str
    age: int


students = [
    {
        "student_id": 1,
        "fullname": "Иванов Иван Иванович",
        "name": "Иван",
        "group": "ПИ-101",
        "age": 19,
    },
    {
        "student_id": 2,
        "fullname": "Петрова Анна Сергеевна",
        "name": "Анна",
        "group": "ПИ-101",
        "age": 20,
    },
    {
        "student_id": 3,
        "fullname": "Сидоров Петр Алексеевич",
        "name": "Петр",
        "group": "ПИ-102",
        "age": 18,
    },
    {
        "student_id": 4,
        "fullname": "Козлова Екатерина Дмитриевна",
        "name": "Екатерина",
        "group": "ПИ-102",
        "age": 19,
    },
    {
        "student_id": 5,
        "fullname": "Смирнов Алексей Владимирович",
        "name": "Алексей",
        "group": "ПИ-103",
        "age": 21,
    },
    {
        "student_id": 6,
        "fullname": "Морозова Ольга Павловна",
        "name": "Ольга",
        "group": "ПИ-103",
        "age": 20,
    },
    {
        "student_id": 7,
        "fullname": "Новиков Дмитрий Андреевич",
        "name": "Дмитрий",
        "group": "ПИ-104",
        "age": 19,
    },
    {
        "student_id": 8,
        "fullname": "Волкова Мария Игоревна",
        "name": "Мария",
        "group": "ПИ-104",
        "age": 18,
    },
    {
        "student_id": 9,
        "fullname": "Зайцев Артем Сергеевич",
        "name": "Артем",
        "group": "ПИ-105",
        "age": 22,
    },
    {
        "student_id": 10,
        "fullname": "Соколова Елена Александровна",
        "name": "Елена",
        "group": "ПИ-105",
        "age": 20,
    },
    {
        "student_id": 11,
        "fullname": "Кузнецов Андрей Викторович",
        "name": "Андрей",
        "group": "ПИ-101",
        "age": 19,
    },
    {
        "student_id": 12,
        "fullname": "Попова Наталья Сергеевна",
        "name": "Наталья",
        "group": "ПИ-102",
        "age": 20,
    },
    {
        "student_id": 13,
        "fullname": "Васильев Олег Иванович",
        "name": "Олег",
        "group": "ПИ-103",
        "age": 21,
    },
    {
        "student_id": 14,
        "fullname": "Михайлова Ирина Петровна",
        "name": "Ирина",
        "group": "ПИ-104",
        "age": 18,
    },
    {
        "student_id": 15,
        "fullname": "Федоров Максим Алексеевич",
        "name": "Максим",
        "group": "ПИ-105",
        "age": 22,
    },
]
