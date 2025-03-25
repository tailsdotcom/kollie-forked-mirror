from unittest.mock import patch

from kollie.cluster.constants import DEFAULT_FLUX_REPOSITORY, KOLLIE_NAMESPACE
from kollie.cluster.git_repository_request import CreateGitRepositoryRequest


@patch("kollie.cluster.git_repository_request.V1ObjectMeta", new=dict)
@patch("kollie.cluster.git_repository_request.V1OwnerReference", new=dict)
def test_create_git_repository_request_body():
    env_name = "test_env"
    branch = "test_branch"
    owner_email = "test@owner.com"
    owner_uid = "test_uid"
    git_repository_name="test_git_repo_name"

    request = CreateGitRepositoryRequest(
        env_name=env_name,
        branch=branch,
        owner_email=owner_email,
        owner_uid=owner_uid,
        git_repository_name=git_repository_name
    )

    assert request.body == {
        "apiVersion": "source.toolkit.fluxcd.io/v1",
        "kind": "GitRepository",
        "metadata": {
            "name": git_repository_name,
            "namespace": KOLLIE_NAMESPACE,
            "labels": {
                "tails-app-stage": "testing",
                "tails-app-environment": env_name,
            },
            "annotations": {
                "tails.com/owner": owner_email,
                "tails.com/tracking-branch": branch,
            },
            "owner_references": [
                {
                    "api_version": "v1",
                    "name": env_name,
                    "block_owner_deletion": True,
                    "uid": owner_uid,
                    "kind": "ConfigMap",
                },
            ],
        },
        "spec": {
            "interval": "5m",
            "ref": {"branch": branch},
            "secretRef": {"name": DEFAULT_FLUX_REPOSITORY},
            "url": f"ssh://git@github.com/tailsdotcom/{DEFAULT_FLUX_REPOSITORY}",
        },
    }
