import os

from .app_template import AppTemplate
from .app_template_source import AppTemplateSource, JsonFileAppTemplateSource


class AppTemplateStore:
    """
    Data store for AppTemplates

    AppTemplates are objects that contains information that kollie needs
    to deploy an application. They are used to generate Kustomizations and
    ImagePolicy resources.

    Args:
        source (AppTemplateSource): Source for AppTemplates

    Returns:
        AppTemplateStore: A new AppTemplateStore
    """

    def __init__(self, source: AppTemplateSource) -> None:
        self._source = source

    def get_by_name(self, app_name: str) -> AppTemplate | None:
        """Returns an AppTemplate by name.

        Args:
            app_name (str): Name of the AppTemplate to return

        Returns:
            AppTemplate: The AppTemplate with the given name
        """
        templates = self._source.load()

        for template in templates:
            if template.app_name == app_name:
                return template

        return None

    def get_all(self) -> list[AppTemplate]:
        """Returns all AppTemplates.

        Returns:
            list[AppTemplate]: All AppTemplates
        """
        return self._source.load()


def get_app_template_store() -> AppTemplateStore:
    """Factory function for AppTemplateStore."""
    json_path = os.environ.get("KOLLIE_APP_TEMPLATE_JSON_PATH", "app_templates.json")

    return AppTemplateStore(source=JsonFileAppTemplateSource(json_path=json_path))
