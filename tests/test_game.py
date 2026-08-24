import pytest

from game import Game, evaluate_guess


def test_evaluate_guess_fully_correct():
    result = evaluate_guess("apple", "apple")

    assert result == ["correct", "correct", "correct", "correct", "correct"]


def test_evaluate_guess_mix_of_results():
    result = evaluate_guess("apple", "aloud")

    assert result == ["correct", "absent", "absent", "absent", "absent"]


def test_evaluate_guess_with_duplicate_letters():
    result = evaluate_guess("apple", "allee")

    assert result == ["correct", "correct", "absent", "absent", "present"]


def test_make_guess_not_in_word_list():
    game = Game("apple", ["apple", "grape", "house"])

    with pytest.raises(ValueError):
        game.make_guess("zzzzz")


def test_game_is_won_after_correct_guess():
    game = Game("apple", ["apple", "grape", "house"])

    game.make_guess("apple")

    assert game.is_won is True


def test_game_is_over_after_six_failed_guesses():
    game = Game("apple", ["apple", "grape", "house", "brick", "chair", "table"])

    for guess in ["grape", "house", "brick", "chair", "table", "grape"]:
        game.make_guess(guess)

    assert game.is_over is True