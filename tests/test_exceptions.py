from kollie.exceptions import (
    KollieConfigError,
    KollieImagePolicyException,
    KollieKustomizationException,
)


def test_kollie_config_error():
    message = "Test message"
    exception = KollieConfigError(message)
    assert str(exception) == message


def test_kollie_image_policy_exception():
    app_name = "Test app"
    env_name = "Test env"
    exception = KollieImagePolicyException(app_name, env_name)
    expected_message = f"Failed to create ImagePolicy for {app_name} in {env_name}"
    assert str(exception) == expected_message


def test_kollie_kustomization_exception():
    action = "Test action"
    app_name = "Test app"
    env_name = "Test env"
    exception = KollieKustomizationException(action, app_name, env_name)
    expected_message = f"Failed to {action} Kustomization for {app_name} in {env_name}"
    assert str(exception) == expected_message
