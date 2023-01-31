from unittest.mock import Mock

import pytest

from libprotools.spam.main import EnviadordeSpam
from libprotools.spam.modelos import Usuario
from libprotools.spam.enviador_de_email import Enviador


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome="Italo", email='italodg9@outlook.com'),
            Usuario(nome="Gomes", email='gomes@outlook.com')
        ],
        [
            Usuario(nome="Italo", email='italodg9@outlook.com')
        ]
    ]
)
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadordeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'italodg9@gmail.com',
        'Spam Curso',
        'Corpo do email'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Italo", email='italodg9@outlook.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadordeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'italodg9@gmail.com',
        'Spam Curso',
        'Corpo do email'
    )
    enviador.enviar.assert_called_once_with(
        'italodg9@gmail.com',
        'italodg9@outlook.com',
        'Spam Curso',
        'Corpo do email'
    )
