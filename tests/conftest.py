import pytest

from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy("Водитель", "voditel@vod.ru", 50000, "Работа связана с вождением", "12345")


@pytest.fixture
def sample_vacancy():
    return Vacancy("Python Developer", "https://example.com/vacancy/1", 100000, "Разработка на Python", 1)


@pytest.fixture
def sample_vacancy_data():
    return [
        {
            "name": "Python Developer",
            "alternate_url": "https://example.com/vacancy/1",
            "salary": {"from": 100000},
            "snippet": {"requirement": "Опыт работы с Python", "responsibility": "Разработка новых функций"},
            "id": "1",
        },
        {
            "name": "Data Scientist",
            "alternate_url": "https://example.com/vacancy/2",
            "salary": None,
            "snippet": None,
            "id": "2",
        },
        {
            "name": "DevOps Engineer",
            "alternate_url": "https://example.com/vacancy/3",
            "salary": {"from": 150000},
            "snippet": {"requirement": None, "responsibility": "Поддержка инфраструктуры"},
            "id": "3",
        },
    ]


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("Junior", "link1", 50000, "desc1", "1"),
        Vacancy("Junior1", "link1", 50000, "desc1", "4"),
        Vacancy("Middle", "link2", 100000, "desc2", "2"),
        Vacancy("Senior", "link3", 150000, "desc3", "3"),
    ]


@pytest.fixture
def sample_vacancies_work():
    return [
        Vacancy("Python Developer", "http://example.com/1", 100000, "Разработка на Python", "1"),
        Vacancy("Java Developer", "http://example.com/2", 90000, "Разработка на Java", "2"),
        Vacancy("Data Scientist", "http://example.com/3", 120000, "Анализ данных и машинное обучение", "3"),
        Vacancy("DevOps Engineer", "http://example.com/4", 110000, "Настройка CI/CD", "4"),
        Vacancy("Frontend Developer", "http://example.com/5", 95000, "Разработка на React", "5"),
    ]


@pytest.fixture
def hh_api():
    return HeadHunterAPI()
