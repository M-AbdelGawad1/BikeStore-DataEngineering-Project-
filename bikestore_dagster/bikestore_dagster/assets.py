from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import bikestore_project_project


@dbt_assets(manifest=bikestore_project_project.manifest_path)
def bikestore_project_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    