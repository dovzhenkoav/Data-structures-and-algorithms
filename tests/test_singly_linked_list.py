import pytest

from DataStructures import SinglyLinkedList


def test_create():
    llst = SinglyLinkedList()
    assert str(llst) == 'SinglyLinkedList()'


def test_append():
    llst = SinglyLinkedList()
    for i in range(10):
        llst.append(i)
    assert str(llst) == 'SinglyLinkedList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)'
    llst = SinglyLinkedList()
    llst.append(None)
    llst.append(2.4)
    llst.append('test')
    assert str(llst) == 'SinglyLinkedList(None, 2.4, test)'


def test_len():
    llst = SinglyLinkedList()
    assert len(llst) == 0
    for i in range(10):
        llst.append(i)
    assert len(llst) == 10


def test_get():
    llst = SinglyLinkedList()
    for i in range(10):
        llst.append(i)
    assert llst[0] == 0
    assert llst[5] == 5
    assert llst[9] == 9
    with pytest.raises(IndexError):
        llst[10]
    with pytest.raises(IndexError):
        llst[45]
    with pytest.raises(IndexError):
        llst[-1]


def test_insert():
    llst = SinglyLinkedList()
    for i in range(3):
        llst.append(i)
    llst.insert(0, 9)
    assert str(llst) == 'SinglyLinkedList(9, 0, 1, 2)'
    llst.insert(1, 9)
    assert str(llst) == 'SinglyLinkedList(9, 9, 0, 1, 2)'
    llst.insert(4, 9)
    assert str(llst) == 'SinglyLinkedList(9, 9, 0, 1, 9, 2)'
    with pytest.raises(IndexError):
        llst.insert(10, 9)
    with pytest.raises(IndexError):
        llst.insert(-1, 9)


def test_delete():
    llst = SinglyLinkedList()
    for i in range(10):
        llst.append(i)
    llst.remove(0)
    assert str(llst) == 'SinglyLinkedList(1, 2, 3, 4, 5, 6, 7, 8, 9)'
    llst.remove(2)
    assert str(llst) == 'SinglyLinkedList(1, 2, 4, 5, 6, 7, 8, 9)'
    llst.remove(7)
    assert str(llst) == 'SinglyLinkedList(1, 2, 4, 5, 6, 7, 8)'
    with pytest.raises(IndexError):
        llst.remove(10)


def test_contains():
    llst = SinglyLinkedList()
    for i in range(10):
        llst.append(i)
    llst.append('qwerty')
    llst.append(0.4)
    assert 0 in llst
    assert 9 in llst
    assert 'qwerty' in llst
    assert 0.4 in llst
    assert 66 not in llst
    assert -1 not in llst
