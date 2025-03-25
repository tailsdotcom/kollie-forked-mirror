from unittest.mock import patch

from kollie.models import KollieEnvironment


@patch("kollie.app.ui.views.envs", autospec=True)
def test_create_env(mock_envs, test_client):
    response = test_client.post(
        "/create",
        data={"env_name": "test_env", "flux_repo_branch": "test_flux_branch"},
        headers={"X-AUTH-REQUEST-EMAIL": "test@owner.com"},
    )

    mock_envs.create_env.assert_called_once_with(
        env_name="test_env",
        flux_repo_branch="test_flux_branch",
        owner_email="test@owner.com"
    )
    assert response.status_code == 200
    assert response.template.name == "/envs/details.jinja2"


@patch("kollie.app.ui.views.applications")
def test_app_detail(mock_apps, test_client):
    response = test_client.get("/env/test_env/test_app")

    mock_apps.get_app.assert_called_once_with(env_name="test_env", app_name="test_app")
    assert response.status_code == 200
    assert response.template.name == "/apps/detail.jinja2"


@patch("kollie.app.ui.views.applications")
def test_app_edit(mock_apps, test_client):
    response = test_client.get("/env/test_env/test_app/edit")

    mock_apps.get_app.assert_called_once_with(env_name="test_env", app_name="test_app")
    assert response.status_code == 200
    assert response.template.name == "/apps/edit.jinja2"


@patch("kollie.app.ui.views.applications")
def test_app_save(mock_apps, test_client):
    response = test_client.post(
        "/env/test_env/test_app/save",
        data={"image_tag_prefix": "main"},
        follow_redirects=False,
    )

    mock_apps.update_app.assert_called_once_with(
        env_name="test_env",
        app_name="test_app",
        attributes=dict(image_tag_prefix="main"),
    )
    assert response.status_code == 302
    assert response.headers["location"] == "/env/test_env/test_app"


@patch("kollie.app.ui.views.envs")
def test_select_bundle_obtains_bundles_from_service(mock_envs, test_client):
    # arrange
    mock_envs.get_env.return_value = KollieEnvironment(
        name="test_env",
        owner_email="test@owner.com",
        apps=[],
        flux_repository_branch=None
    )

    # act
    response = test_client.get("/env/foo/add-bundle")

    # assert
    mock_envs.get_available_app_bundles.assert_called_once()
    assert response.status_code == 200
    assert response.template.name == "/apps/add_bundle.jinja2"

    assert response.context["environment"].name == "test_env"
    assert response.context["environment"].owner_email == "test@owner.com"


@patch("kollie.app.ui.views.envs")
def test_select_bundle_raises_404_when_env_does_not_exist(mock_envs, test_client):
    # arrange
    mock_envs.get_env.return_value = None

    # act

    response = test_client.get("/env/foo/add-bundle")

    # assert
    assert response.status_code == 404


@patch("kollie.app.ui.views.envs")
def test_deploy_bundle_calls_service_method_correctly(mock_envs, test_client):
    # arrange
    mock_envs.get_env.return_value = KollieEnvironment(
        name="test_env",
        owner_email="test@owner.com",
        apps=[],
        flux_repository_branch=None
    )

    # act
    response = test_client.post(
        "/env/foo/add-bundle",
        data={"bundle_name": "test_bundle"},
        headers={"X-AUTH-REQUEST-EMAIL": "test@owner.com"},
    )

    # assert
    assert response.status_code == 200
    mock_envs.install_bundle.assert_called_once_with(
        env_name="foo", bundle_name="test_bundle", owner_email="test@owner.com"
    )


@patch("kollie.app.ui.views.envs")
def test_deploy_bundle_404(mock_envs, test_client):
    # arrange
    mock_envs.get_env.return_value = None

    # act
    response = test_client.post(
        "/env/foo/add-bundle",
        data={"bundle_name": "test_bundle"},
        headers={"X-AUTH-REQUEST-EMAIL": "test@owner.com"},
    )

    # assert
    assert response.status_code == 404
    mock_envs.deploy_app_bundle.assert_not_called()
