import simple_math
import pytest

@pytest.mark.parametrize("n, m, add", [(1, 2, 3),
                                           (4, 5, 9),
                                           (10, 201, 211)])

def test_add(n,m, add):
    assert simple_math.simple_add(n, m) == add

@pytest.mark.parametrize("a, b, mult", [(1, 2, 2),
                                           (4, 5, 20),
                                           (10, 201, 2010)])

def test_mult(a, b, mult):
    assert simple_math.simple_mult(a, b) == mult


@pytest.mark.parametrize("c, d, div",       [(2, 1, 2),
                                           (20, 5, 4),
                                           (2010, 201, 10)])

def test_div(c, d, div):
    assert simple_math.simple_div(c, d) == div

@pytest.mark.parametrize("e, f, sub",       [(2, 1, 1),
                                           (20, 5, 15),
                                           (2010, 201, 1809)])

def test_sub(e, f, sub):
    assert simple_math.simple_sub(e, f) == sub

@pytest.mark.parametrize("g, h, i, pol1",       [(3, 2, 1, 5),
                                           (20, 5, 4, 85),
                                           (201, 55, 10, 2065)])

def test_pol1(g, h, i, pol1):
    assert simple_math.poly_first(g, h, i) == pol1

@pytest.mark.parametrize("j, k, l, o, pol2",       [(3, 2, 1, 5, 50),
                                           (20, 5, 4, 85, 34085),
                                           (201, 55, 10, 2065, 83430130)])

def test_pol1(j, k, l, o, pol2):
    assert simple_math.poly_second(j, k, l, o) == pol2