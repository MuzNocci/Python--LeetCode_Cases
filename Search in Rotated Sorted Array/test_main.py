from main import Solution
    


def test_search_1():

    assert Solution.search(Solution, [4,5,6,7,0,1,2], 0) == 4, 'Não passou no teste 1'


def test_search_2():

    assert Solution.search(Solution, [4,5,6,7,0,1,2], 3) == -1, 'Não passou no teste 2'


def test_search_3():

    assert Solution.search(Solution, [1], 0) == -1, 'Não passou no teste 3'


def test_search_4():

    assert Solution.search(Solution, [1,2,4,0,5], 0) == 3, 'Não passou no teste 4'