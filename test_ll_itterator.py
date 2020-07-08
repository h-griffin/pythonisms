import pytest
from ll_itterator import Linked_list

def test_for_in():
    foods = Linked_list(('apple', 'banana', 'carrot'))
    foods_list = []

    for food in foods:
        foods_list.append(food)
    assert foods_list == ['apple', 'banana', 'carrot']

# def test_ll_comprehension():
#     foods = Linked_list(('apple', 'banana', 'carrot'))
#     cap_foods = [food.upper() for food in foods]
#     assert list(foods) == ['APPLE', 'BANANA', 'CARROT']


def test_list_case():
    foods_list = ['apple', 'banana', 'carrot']
    foods = Linked_list(foods_list)
    assert list(foods) == foods_list

def test_case():
    num_range = range(1,20+1)
    nums = Linked_list(num_range)
    assert len(nums) == 20

def test_filter():
    nums = Linked_list(range(1, 21))
    odds = [num for num in nums if num % 2]
    assert odds == [1,3,5,7,9,11,13,15,17,19]

def test_next():
    foods = Linked_list(['apple', 'banana', 'carrot'])

    itterator = iter(foods)
    assert next(itterator) == 'apple'
    assert next(itterator) == 'banana'
    assert next(itterator) == 'carrot'

def test_stop_itteration():
    foods = Linked_list(['apple', 'banana', 'carrot'])
    itterator = iter(foods)
    with pytest.raises(StopIteration):
        while True:
            food = next(itterator)

def test_range():
    num_range = range(1,20+1)
    nums = Linked_list(num_range)
    assert len(nums) == 20

def test_str():
    foods = Linked_list(['apple', 'banana', 'carrot'])
    assert str(foods == '[ apple ] -> [ banana ] -> [ carrot ] -> None')

def test_equals():
    lla = Linked_list(['apple', 'banana', 'carrot'])
    llb = Linked_list(['apple', 'banana', 'carrot'])
    assert lla == llb

def test_get_item():
    foods = Linked_list(['apple', 'banana', 'carrot'])
    assert foods[0] == 'apple'

def test_get_item_out_of_range():
    foods = Linked_list(['apple', 'banana', 'carrot'])
    with pytest.raises(IndexError):
        foods[100]