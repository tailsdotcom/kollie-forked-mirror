from kollie.persistence import AppTemplate, ImageRepositoryRef


def test_app_template_from_dict():
    data = {
        "app_name": "test_app",
        "label": "test_label",
        "git_repository_name": "cat-apps-k8s",
        "git_repository_path": "bob/builder",
        "image_repository_ref": {"name": "test_repo", "namespace": "test_namespace"},
        "default_image_tag_prefix": "things-main",
    }

    app_template = AppTemplate.from_dict(data)

    assert isinstance(app_template, AppTemplate)
    assert isinstance(app_template.image_repository_ref, ImageRepositoryRef)

    assert app_template.app_name == "test_app"
    assert app_template.label == "test_label"
    assert app_template.git_repository_name == "cat-apps-k8s"
    assert app_template.git_repository_path == "bob/builder"
    assert app_template.image_repository_ref.name == "test_repo"
    assert app_template.image_repository_ref.namespace == "test_namespace"
    assert app_template.default_image_tag_prefix == "things-main"


def test_app_template_git_repository_name_default():
    data = {
        "app_name": "test_app",
        "label": "test_label",
        "git_repository_path": "bob/builder",
        "image_repository_ref": {"name": "test_repo", "namespace": "test_namespace"},
        "default_image_tag_prefix": "main",
    }

    app_template = AppTemplate.from_dict(data)

    assert isinstance(app_template, AppTemplate)
    assert isinstance(app_template.image_repository_ref, ImageRepositoryRef)

    assert app_template.app_name == "test_app"
    assert app_template.label == "test_label"
    assert app_template.git_repository_name == "test-repo"
    assert app_template.git_repository_path == "bob/builder"
    assert app_template.image_repository_ref.name == "test_repo"
    assert app_template.image_repository_ref.namespace == "test_namespace"
    assert app_template.default_image_tag_prefix == "main"


def test_app_template_image_tag_prefix_default():
    data = {
        "app_name": "test_app",
        "label": "test_label",
        "git_repository_name": "test-flux-repository",
        "git_repository_path": "bob/builder",
        "image_repository_ref": {"name": "test_repo", "namespace": "test_namespace"},
        "default_image_tag_prefix": "main",
    }

    app_template = AppTemplate.from_dict(data)

    assert isinstance(app_template, AppTemplate)
    assert isinstance(app_template.image_repository_ref, ImageRepositoryRef)

    assert app_template.app_name == "test_app"
    assert app_template.label == "test_label"
    assert app_template.git_repository_name == "test-flux-repository"
    assert app_template.git_repository_path == "bob/builder"
    assert app_template.image_repository_ref.name == "test_repo"
    assert app_template.image_repository_ref.namespace == "test_namespace"
    assert app_template.default_image_tag_prefix == "main"
