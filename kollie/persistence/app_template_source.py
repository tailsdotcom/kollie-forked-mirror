import json
from typing import Protocol

from .app_template import AppTemplate


class AppTemplateSource(Protocol):
    """Protocol for AppTemplateSource."""

    def load(self) -> list[AppTemplate]: ...


class JsonFileAppTemplateSource:
    """Source for AppTemplates from a JSON file."""

    def __init__(self, json_path: str) -> None:
        """Initializes a JsonFileAppTemplateSource.

        Args:
            file_path (str): Path to the JSON file
        """
        self._json_path = json_path

    def load(self) -> list[AppTemplate]:
        """Loads AppTemplates from a JSON file.

        Returns:
            list[AppTemplate]: List of app templates
        """
        try:
            with open(self._json_path, "r") as source_file:
                content = source_file.read()
                if not content:
                    # File is empty
                    return []
                templates = json.loads(content)
        except json.JSONDecodeError:
            # File is not empty, but contains malformed JSON
            raise ValueError(f"File {self._json_path} contains malformed JSON")

        return [AppTemplate.from_dict(template) for template in templates]
