from src.main import *
from unittest.mock import patch

def teste_root():
    assert root() == {"message": "Hello World"}


def test_funcaoteste():
    with patch('radom.radint', return_value=12345):
        result = funcaoteste()

    assert result == {"teste": True, "num_aleatorio": 12345 }

def test_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    assert  estudante_teste == create_estudante()


def test_update_estudante_positivo():
    assert not update_estudante(-5)

def test_update_estudante_negativo():
    assert update_estudante(10)

def teste_delete_estudante_negativo():
    assert not delete_estudante(-5)

def teste_delete_estudante_positivo():
    assert delete_estudante(10)
