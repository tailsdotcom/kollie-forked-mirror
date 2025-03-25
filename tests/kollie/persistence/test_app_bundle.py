from kollie.persistence.app_bundle import AppBundle, AppBundleStore
from kollie.persistence.item_source import JsonItemSource


def _build_app_bundle_store(bundle_json: str) -> AppBundleStore:
    """
    Helper function to build an AppBundleStore with the given bundle JSON and app templates.
    app_templates is a list of app names that will be used to generate AppTemplates.
    """
    bundle_source = JsonItemSource(item_type=AppBundle, json_str=bundle_json)
    return AppBundleStore(app_bundle_source=bundle_source)


def test_app_bundle_store_get_all_bundles():
    # arrange
    bundle_json = """
    [
        {"name": "bundle1", "description": "bundle1 description", "apps": ["app1", "app2"]},
        {"name": "bundle2", "description": "bundle2 description", "apps": ["app3", "app4"]}
    ]
    """

    # act
    bundle_store = AppBundleStore(
        app_bundle_source=JsonItemSource(item_type=AppBundle, json_str=bundle_json)
    )

    bundles = bundle_store.get_all_bundles()

    # assert
    assert len(bundles) == 2
    assert sorted(["bundle1", "bundle2"]) == sorted([bundle.name for bundle in bundles])


def test_app_bundle_store_get_bundle():
    # arrange
    bundle_json = """
    [
        {"name": "bundle1", "description": "bundle1 description", "apps": ["app1", "app2"]},
        {"name": "bundle2", "description": "bundle2 description", "apps": ["app3", "app4"]}
    ]
    """

    # act
    bundle_store = AppBundleStore(
        app_bundle_source=JsonItemSource(item_type=AppBundle, json_str=bundle_json)
    )

    bundle = bundle_store.get_bundle("bundle1")

    # assert
    assert bundle is not None
    assert bundle.name == "bundle1"
    assert bundle.description == "bundle1 description"
    assert sorted(["app1", "app2"]) == sorted([app for app in bundle.apps])


def test_app_bundle_store_get_bundle_not_found():
    # arrange
    bundle_json = """
    [
        {"name": "bundle1", "description": "bundle1 description", "apps": ["app1", "app2"]},
        {"name": "bundle2", "description": "bundle2 description", "apps": ["app3", "app4"]}
    ]
    """

    # act
    bundle_store = AppBundleStore(
        app_bundle_source=JsonItemSource(item_type=AppBundle, json_str=bundle_json)
    )

    bundle = bundle_store.get_bundle("bundle3")

    # assert
    assert bundle is None
