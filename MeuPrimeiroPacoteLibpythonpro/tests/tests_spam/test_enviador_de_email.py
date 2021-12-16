import pytest

from MeuPrimeiroPacoteLibpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['arthur.regismais@hotmail.com', 'andressamdm.@hotmail.com'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
            remetente,
            'adevar.mais@hotmail.com',
            'Fotos das obras da firma',
            'Ta faltando fotos mais recentes.'
        )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'andressamdm'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'adevar.mais@hotmail.com',
            'Fotos das obras da firma',
            'Ta faltando fotos mais recentes.'
        )
