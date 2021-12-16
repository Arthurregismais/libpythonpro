import pytest

from MeuPrimeiroPacoteLibpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['arthur.regismais@hotmail.com', 'andressamdm.@hotmail.com'])
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
            destinatario,
            'adevar.mais@hotmail.com',
            'Fotos das obras da firma',
            'Ta faltando fotos mais recentes.'
        )
    assert destinatario in resultado
