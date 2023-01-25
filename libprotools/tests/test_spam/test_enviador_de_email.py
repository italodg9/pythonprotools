import pytest

from libprotools.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['italodg9@outlook.com', 'joao@gmail.com']
)
def test_remetende(remetente):
    enviador = Enviador()

    resultado = enviador.enviar(
        remetente,
        'italodg9@gmail.com',
        'Curso Python Pro',
        'Teste aula pythonPro'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['italodg9', '']
)
def test_remetende(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'italodg9@gmail.com',
            'Curso Python Pro',
            'Teste aula pythonPro'
        )
