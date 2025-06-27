from src.vacancies_processing import VacProcessing


def test_get_top_vacancies(sample_vacancies_work):
    top_3 = VacProcessing.get_top_vacancies(sample_vacancies_work, 3)
    assert len(top_3) == 3
    assert [v.salary for v in top_3] == [120000, 110000, 100000]


def test_sort_vacancies(sample_vacancies_work):
    sorted_vacancies = VacProcessing.sort_vacancies(sample_vacancies_work)
    assert len(sorted_vacancies) == 5
    assert sorted_vacancies[0].job_title == "Java Developer"
    assert sorted_vacancies[4].job_title == "Data Scientist"


def test_print_vacancies(sample_vacancies_work):
    result = VacProcessing.print_vacancies(sample_vacancies_work[:2])
    assert result == ("ID номер:             1\n"
    "Название вакансии:    Python Developer\n"
    "Ссылка на вакансию:   http://example.com/1\n"
    "Размер зарплаты:      100000\n"
    "Описание вакансии:    Разработка на Python\n"
    "--------------------------------------------------\n"
    "ID номер:             2\n"
    "Название вакансии:    Java Developer\n"
    "Ссылка на вакансию:   http://example.com/2\n"
    "Размер зарплаты:      90000\n"
    "Описание вакансии:    Разработка на Java\n"
    "--------------------------------------------------")


def test_filter_vacancies(sample_vacancies_work):
    result = VacProcessing.filter_vacancies(sample_vacancies_work, "Анализ")
    assert len(result) == 1
    assert result[0].job_title == "Data Scientist"


def test_get_vacancies_by_salary(sample_vacancies_work):
    result = VacProcessing.get_vacancies_by_salary(sample_vacancies_work, "100000 -110000")
    assert len(result) == 2
    assert result[0].job_title == "Python Developer"
    assert result[1].job_title == "DevOps Engineer"