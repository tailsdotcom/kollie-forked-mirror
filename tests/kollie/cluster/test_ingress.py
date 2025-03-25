from kollie.cluster.ingress import get_ingress


def test_get_ingresses(mocker):
    mock_api = mocker.patch("kubernetes.client.NetworkingV1Api", autospec=True)
    mock_list_namespaced_ingress = mock_api.return_value.list_ingress_for_all_namespaces

    env_name = "test-env"
    app_name = "test-app"
    get_ingress(env_name, app_name)

    mock_list_namespaced_ingress.assert_called_once_with(
        label_selector=f"tails-environment={env_name},tails-app-name={app_name}",
    )
