from MeuPrimeiroPacoteLibpythonpro.spam.modelo import Usuario


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='Arthur', email='arthur.regismais@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(conexao, sessao):
    usuarios = [Usuario(nome='Arthur', email='arthur.regismais@hotmail.com'),
                Usuario(nome='Adevar', email='arthur.regismais@hotmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
