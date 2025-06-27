from unittest.mock import patch

from src.user_interaction import UserInteraction


@patch("builtins.input", return_value="test")
def test_check_input(mock_input):
    result = UserInteraction.check_input("Введите что-то")
    assert result == "test"
    mock_input.assert_called_once()


@patch("builtins.input", side_effect=["", "valid"])
def test_check_input_empty_then_valid(mock_input):
    result = UserInteraction.check_input("Введите что-то")
    assert result == "valid"
    assert mock_input.call_count == 2


@patch("builtins.input", return_value="y")
def test_result_for_next_yes(mock_input, capsys):
    vacancies = [1, 2, 3]
    result = [4, 5]

    UserInteraction.result_for_next(vacancies, result)

    captured = capsys.readouterr()
    assert vacancies == [4, 5]
    assert "Использовать результат для дальнейшей обработки?" in captured.out


@patch("builtins.input", return_value="n")
def test_result_for_next_no(mock_input, capsys):
    vacancies = [1, 2, 3]
    result = [4, 5]

    UserInteraction.result_for_next(vacancies, result)

    captured = capsys.readouterr()
    assert vacancies == [1, 2, 3]
    assert "Использовать результат для дальнейшей обработки?" in captured.out
