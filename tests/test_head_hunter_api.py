from unittest.mock import patch


@patch("requests.get")
def test_load_vacancies_success(mock_get, hh_api):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "items": [{"id": 1, "name": "Python Developer"}, {"id": 2, "name": "Data Scientist"}]
    }

    keyword = "Python"
    result = hh_api.load_data(keyword)

    assert len(result) == 40
    assert mock_get.call_count == 20
    assert result[0]["name"] == "Python Developer"