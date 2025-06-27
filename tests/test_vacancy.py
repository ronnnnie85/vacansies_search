from src.vacancy import Vacancy


def test_vacancy(vacancy):
    assert vacancy.job_title == "Водитель"
    assert vacancy.link_to_the_vacancy == "voditel@vod.ru"
    assert vacancy.salary == 50000
    assert vacancy.description == "Работа связана с вождением"
    assert vacancy.id == 12345


def test_cast_to_dict(sample_vacancy):
    Vacancy.cast_to_dict(sample_vacancy)
    result = sample_vacancy.cast_to_dict()
    assert result["job_title"] == sample_vacancy._Vacancy__job_title
    assert result["link_to_the_vacancy"] == sample_vacancy._Vacancy__link_to_the_vacancy
    assert result["salary"] == sample_vacancy._Vacancy__salary
    assert result["description"] == sample_vacancy._Vacancy__description
    assert result["id"] == sample_vacancy._Vacancy__id


def test_cast_to_object_list_correct_conversion(sample_vacancy_data):
    result = Vacancy.cast_to_object_list(sample_vacancy_data)

    assert result[0]._Vacancy__job_title == "Python Developer"
    assert result[0]._Vacancy__link_to_the_vacancy == "https://example.com/vacancy/1"
    assert result[0]._Vacancy__salary == 100000
    assert result[0]._Vacancy__description == "Разработка новых функций\nОпыт работы с Python"
    assert result[0]._Vacancy__id == 1

    assert result[1]._Vacancy__job_title == "Data Scientist"
    assert result[1]._Vacancy__link_to_the_vacancy == "https://example.com/vacancy/2"
    assert result[1]._Vacancy__salary == 0
    assert result[1]._Vacancy__description == "\n"
    assert result[1]._Vacancy__id == 2

    assert result[2]._Vacancy__job_title == "DevOps Engineer"
    assert result[2]._Vacancy__link_to_the_vacancy == "https://example.com/vacancy/3"
    assert result[2]._Vacancy__salary == 150000
    assert result[2]._Vacancy__description == ""
    assert result[2]._Vacancy__id == 3


def test_vacancy_repr(vacancy):
    assert repr(vacancy) == ("Vacancy(Водитель, voditel@vod.ru, 50000, Работа связана с вождением, "
                             "12345)")


def test_vacancy_str(vacancy):
    assert str(vacancy) == (f"ID номер:             12345\n"
                            f"Название вакансии:    Водитель\n"
                            f"Ссылка на вакансию:   voditel@vod.ru\n"
                            f"Размер зарплаты:      50000\n"
                            f"Описание вакансии:    Работа связана с вождением")


def test_le(sample_vacancies):
    assert sample_vacancies[0] <= sample_vacancies[2]
    assert sample_vacancies[0] <= 100000


def test_ge(sample_vacancies):
    assert sample_vacancies[2] >= sample_vacancies[0]
    assert sample_vacancies[2] >= 50000


def test_eq(sample_vacancies):
    assert sample_vacancies[0] == sample_vacancies[1]
    assert sample_vacancies[0] == 50000


def test_ne(sample_vacancies):
    assert sample_vacancies[0] != sample_vacancies[2]
    assert sample_vacancies[0] != 100000


def test_lt(sample_vacancies):
    assert sample_vacancies[0] < sample_vacancies[2]
    assert sample_vacancies[0] < 100000

def test_gt(sample_vacancies):
    assert sample_vacancies[2] > sample_vacancies[0]
    assert sample_vacancies[2] > 50000