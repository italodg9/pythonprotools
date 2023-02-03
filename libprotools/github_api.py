import requests


def buscar_avatar(usuario):
    """
    :param usuario: busca um usuario no git hub
    :return: str com o id e com o avatar
    """

    url = f'https://api.github.com/users/{usuario}'
    busca = requests.get(url)
    return busca.json()['avatar_url']
