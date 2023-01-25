from libprotools.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome="Italo", email= 'italodg9@outlook.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome="Italo", email='italodg9@outlook.com'),
        Usuario(nome="Gomes", email='italodg9@outlook.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
