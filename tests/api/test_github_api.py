import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name'] 


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0
    

 
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
\
    
@pytest.mark.api
def test_repo_has_metadata(github_api):
    r = github_api.get_metadata('octocat', 'Hello-World')
    assert 'full_name' in r, f"Response was: {r}"  # Перевірка наявності повної назви репозиторію
    assert r['full_name'] == 'octocat/Hello-World', f"Response was: {r}"

@pytest.mark.api
def test_repo_does_not_exist(github_api):
    r = github_api.get_metadata('octocat', 'nonexistent-repo')
    assert 'message' in r and r['message'] == 'Not Found', f"Response was: {r}"

# Нові тести для перевірки GitHub Tags

@pytest.mark.api
def test_has_tags(github_api):
    r = github_api.get_tags('github', 'hub')
    assert len(r) > 0, f"Response was: {r}"  # Перевірка наявності хоча б одного тегу

@pytest.mark.api
def test_does_not_have_tags(github_api):
    r = github_api.get_tags('github', 'nonexistent-repo')
    assert 'message' in r and r['message'] == 'Not Found', f"Response was: {r}"      