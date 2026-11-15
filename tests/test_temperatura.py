import pytest

from conversor.temperatura import celsius_para_fahrenheit, fahrenheit_para_celsius


@pytest.mark.parametrize("celsius, esperado", [(0, 32), (100, 212), (-40, -40), (37, 98.6)])
def test_celsius_para_fahrenheit(celsius, esperado):
    assert celsius_para_fahrenheit(celsius) == pytest.approx(esperado)


@pytest.mark.parametrize("fahrenheit, esperado", [(32, 0), (212, 100), (-40, -40), (98.6, 37)])
def test_fahrenheit_para_celsius(fahrenheit, esperado):
    assert fahrenheit_para_celsius(fahrenheit) == pytest.approx(esperado)
