from MeuPrimeiroPacoteLibpythonpro.spam.db import Conexao
from MeuPrimeiroPacoteLibpythonpro.spam.modelo import Usuario


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Arthur')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.rollback()
    sessao.fechar()
    conexao.fechar()


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Arthur'), Usuario(nome='Adevar')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.rollback()
    sessao.fechar()
    conexao.fechar()
