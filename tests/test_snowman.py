import pytest
from unittest.mock import patch
from my_first_package.snowman import choose_word, display, game  

def test_choose_word():
    word_list = ["apple", "banana"]
    with patch('random.choice', return_value='apple'):
        assert choose_word(word_list) == 'apple'

def test_display():
    assert display("apple", ["a", "p"]) == "app__"
    
def test_game_won():
    word_list = ["apple"]
    guess_list = ["a", "p", "l", "e"]
    assert game(word_list, guess_list) == ["You've guessed the word: apple"]

def test_game_lost():
    word_list = ["apple"]
    guess_list = ["b", "c", "d", "f", "g", "h"]
    assert game(word_list, guess_list) == ["Game over"]
