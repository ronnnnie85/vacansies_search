import json
from unittest.mock import patch, mock_open

from src.json_saver import JsonSaver
from src.vacancy import Vacancy


def test_open_file_read_empty_file():
    with (patch("os.path.exists") as mock_exists,
          patch("os.path.getsize") as mock_getsize):
        mock_exists.return_value = True
        mock_getsize.return_value = 0

        saver = JsonSaver("test.json")
        result = saver.open_file_read("test.json")
        assert result == []


def test_open_file_read_non_empty_file():
    test_data = [{"id": 1, "title": "Test"}]
    with (patch("os.path.exists") as mock_exists,
          patch("os.path.getsize") as mock_getsize,
          patch("builtins.open", mock_open(read_data=json.dumps(test_data)))):
        mock_exists.return_value = True
        mock_getsize.return_value = 10

        saver = JsonSaver("test.json")
        result = saver.open_file_read("test.json")
        assert result == test_data


def test_add_vacancy_to_empty_file():
    vacancy_data = {
        "id": 1,
        "job_title": "Python Developer",
        "link_to_the_vacancy": "http://example.com",
        "salary": 100000,
        "description": "Python developer job"
    }
    vacancy = Vacancy(**vacancy_data)

    written_data = []

    def mock_write(data):
        written_data.append(data.strip())
        return len(data)

    mock_file = mock_open()
    mock_file.return_value.write = mock_write

    with patch("builtins.open", mock_file):
        saver = JsonSaver("test.json")
        saver.add_vacancy(vacancy)

        mock_file.assert_called_once_with("test.json", "w", encoding="utf-8")

        assert len(written_data) == 26

        parsed_data = json.loads("".join(written_data))
        expected_data = [vacancy_data]

        assert parsed_data == expected_data


def test_get_vacancy_not_exists():
    with patch.object(JsonSaver, "open_file_read", return_value=[]):
        saver = JsonSaver("test.json")
        result = saver.get_vacancy(999)
        assert result is None


def test_get_vacancy_exists():
    vacancy_data = {"id": 1, "job_title": "Python Developer", "link_to_the_vacancy": "", "salary": 0, "description": ""}
    with patch.object(JsonSaver, "open_file_read", return_value=[vacancy_data]):
        saver = JsonSaver("test.json")
        result = saver.get_vacancy(1)
        assert result is not None
        assert result.id == 1
        assert result.job_title == "Python Developer"


def test_delete_existing_vacancy():
    vacancies = [
        {
            "id": 1,
            "job_title": "To Delete",
            "link_to_the_vacancy": "http://delete.com",
            "salary": 50000,
            "description": "To be deleted"
        },
        {
            "id": 2,
            "job_title": "To Keep",
            "link_to_the_vacancy": "http://keep.com",
            "salary": 100000,
            "description": "Should remain"
        }
    ]

    written_data = []

    def mock_write(data):
        written_data.append(data.strip())
        return len(data)

    mock_file = mock_open()
    mock_file.return_value.write = mock_write

    with (patch.object(JsonSaver, "open_file_read", return_value=vacancies),
        patch("builtins.open", mock_file)):
        saver = JsonSaver("test.json")
        result = saver.delete_vacancy(1)

        assert result is True

        assert len(written_data) == 26

        parsed_data = json.loads("".join(written_data))

        assert len(parsed_data) == 1
        assert parsed_data[0]["id"] == 2
        assert parsed_data[0]["job_title"] == "To Keep"