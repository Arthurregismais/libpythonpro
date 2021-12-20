from unittest.mock import Mock
import pytest
from MeuPrimeiroPacoteLibpythonpro.spam.main import EnviadorDeSpam
from MeuPrimeiroPacoteLibpythonpro.spam.modelo import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Arthur', email='arthur.regismais@hotmail.com'),
            Usuario(nome='Adevar', email='adevar.regismais@hotmail.com')
        ],
        [
            Usuario(nome='Arthur', email='arthur.regismais@hotmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'arthur.regismais@hotmail.com',
        'Fotos das obras da firma',
        'Ainda não recebi as fotos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Arthur', email='arthur.regismais@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'adevar.mais@hotmail.com',
        'Fotos das obras da firma',
        'Ainda não recebi as fotos'
    )
    enviador.enviar.assert_called_once_with(
        'adevar.mais@hotmail.com',
        'arthur.regismais@hotmail.com',
        'Fotos das obras da firma',
        'Ainda não recebi as fotos'
    )
