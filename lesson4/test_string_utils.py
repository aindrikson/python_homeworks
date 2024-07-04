import pytest
from string_utlis import StringUtils

utils = StringUtils()

#capitilize
@pytest.mark.parametrize('input, result', [
    ("test", "Test"),
    ("test skypro", "Test skypro"),
    ("123", "123"),
    ("", ""),
    ("  ", "  "),
    ("1test", "1test"),
    ])
def test_capitilize(input, result):
    utils = StringUtils ()
    res = utils.capitilize(input)
    assert res == result

#trim
@pytest.mark.parametrize('input, result', [
    ("  test", "test"),
    ("  test skypro", "test skypro"),
    ("  test  ", "test  "),
    (" -", "-")
    ])
def test_trim(input, result):
    utils = StringUtils ()
    res = utils.trim(input)
    assert res == result

@pytest.mark.xfail()
def test_trim_negative():
    assert utils.trim("312") == "312"
    assert utils.trim("  test") == "  test"
#to list
@pytest.mark.parametrize('input, delimeter, result', [
    ("наушники,клава,мышка", ",", ["наушники", "клава", "мышка"]),
    ("1|2|3|4", "|", ["1", "2", "3","4"]),
    ("", None, []),
    ("банан,яблоко,вишня", None, ["банан", "яблоко", "вишня"]),
    ])
def test_to_list(input, delimeter, result):
    if delimeter is None:
        res = utils.to_list(input)
    else:
        res = utils.to_list(input, delimeter)
    assert res == result

#contains
@pytest.mark.parametrize('input, symbol, result', [
    ("стол", "о", True),
    ("sport", "r", True),
    ("1212", "0", False),
    ("test", "", True),
    ])
def test_contains (input, symbol, result):
    res = utils.contains(input, symbol)
    assert res == result

#delete symbol
@pytest.mark.parametrize('input, symbol, result', [
    ("ручка", "у", "рчка"),
    ("daily", "d", "aily"),
    ("1212", "2", "11"),
   # ("test", "e", "test"),
    ("", "", ""),
    ("стул", "", "стул"),
    ])
def test_delete_symbol (input, symbol, result):
    res = utils.delete_symbol(input, symbol)
    assert res == result

#starts with
@pytest.mark.parametrize('input, symbol, result', [
    ("стол", "с", True),
    ("sport", "s", True),
    ("1212", "3", False),
    ("test", "", True),
    ])
def test_starts_with (input, symbol, result):
    res = utils.starts_with(input, symbol)
    assert res == result


#end with
@pytest.mark.parametrize('input, symbol, result', [
    ("стол", "л", True),
    ("sport", "t", True),
    ("1212", "3", False),
    ("test", "", True),
    ])
def test_end_with (input, symbol, result):
    res = utils.end_with(input, symbol)
    assert res == result

#is empty
@pytest.mark.parametrize('input, result', [
    ("",  True),
    ("  ", True),
    ("тут не пусто",  False),
    ("тут тоже не пусто   ", False),
    ])
def test_is_empty (input, result):
    res = utils.is_empty(input)
    assert res == result

#list to string
@pytest.mark.parametrize('input, joiner, result', [
    (["наушники", "клава", "мышка"], ",","наушники,клава,мышка"),
    (["1", "2", "3","4"], "|", "1|2|3|4"),
    ([], None, ""),
    (["банан", "яблоко", "вишня"], None, "банан, яблоко, вишня"),
    ])
def test_list_to_string(input, joiner, result):
    if joiner is None:
        res = utils.list_to_string(input)
    else:
        res = utils.list_to_string(input, joiner)
    assert res == result