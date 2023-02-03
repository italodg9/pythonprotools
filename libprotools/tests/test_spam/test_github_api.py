from unittest.mock import Mock

import pytest

from libprotools import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/108771297?v=4'
    resp_mock.json.return_value = {
        'login': 'italodg9', 'id': 108771297,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libprotools.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('italodg9')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('italo')
    assert "https://avatars.githubusercontent.com/u/97863511?v=4" == url
