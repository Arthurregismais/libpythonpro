import pytest

from MeuPrimeiroPacoteLibpythonpro.spam.enviador_de_email import Enviador
from MeuPrimeiroPacoteLibpythonpro.spam.main import EnviadorDeSpam
from MeuPrimeiroPacoteLibpythonpro.spam.modelo import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.parametros_de_envio = None
        self.qtd_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'arthur.regismais@hotmail.com',
        'Fotos das obras da firma',
        'Ainda não recebi as fotos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Arthur', email='arthur.regismais@hotmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'adevar.mais@hotmail.com',
        'Fotos das obras da firma',
        'Ainda não recebi as fotos'
    )
    assert enviador.parametros_de_envio == (
        'adevar.mais@hotmail.com',
        'arthur.regismais@hotmail.com',
        'Fotos das obras da firma',
        'Ainda não recebi as fotos'
    )
