import pytest
from unittest.mock import Mock
from MeuPrimeiroPacoteLibpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = "https://avatars.githubusercontent.com/u/89051127?v=4"
    resp_mock.json.return_value = {
        "login": "Arthurregismais", "id": 89051127, "node_id": "MDQ6VXNlcjg5MDUxMTI3",
        "avatar_url": url
    }
    get_mocker = mocker.patch('MeuPrimeiroPacoteLibpythonpro.github_api.requests.get')
    get_mocker.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.busca_avatar('Arthurregismais')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.busca_avatar('Arthurregismais')
    assert 'https://avatars.githubusercontent.com/u/89051127?v=4' == url
