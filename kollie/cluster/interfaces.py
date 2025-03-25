from typing import Protocol


class ClusterObjectReference(Protocol):
    """
    Interface for ClusterObjectReference
    """

    @property
    def name(self) -> str: ...

    @property
    def namespace(self) -> str: ...


class AppTemplate(Protocol):
    """
    Interface for AppTemplate
    """

    @property
    def app_name(self) -> str: ...

    @property
    def label(self) -> str: ...

    @property
    def default_image_tag_prefix(self) -> str: ...

    @property
    def git_repository_name(self) -> str: ...

    @property
    def git_repository_path(self) -> str: ...

    @property
    def image_repository_ref(self) -> ClusterObjectReference: ...
