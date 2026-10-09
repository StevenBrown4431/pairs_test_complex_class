from lib.most_often import *

def test_check_starting_list():
    most_often = MostOften(["cake"])
    assert most_often.starting_list == ["cake"]

def test_add_new_item():
    most_often = MostOften(["cake"])
    most_often.add_new("biscuit")
    assert most_often.starting_list == ["cake", "biscuit"]

def test_multiple_of_item():
    most_often = MostOften(["cake"])
    most_often.add_new("biscuit")
    most_often.add_new("biscuit")
    assert most_often.starting_list == ["cake", "biscuit", "biscuit"]

def test_for_unique_items():
    most_often = MostOften(["cake"])
    most_often.add_new("biscuit")
    most_often.add_new("biscuit")
    assert most_often.get_most_often() == "biscuit"

def test_no_clear_winner():
    most_often = MostOften(["cake"])
    most_often.add_new("biscuit")
    assert most_often.get_most_often() == "no clear winner"