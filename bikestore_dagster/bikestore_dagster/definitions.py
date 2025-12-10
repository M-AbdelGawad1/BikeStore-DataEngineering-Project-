from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import bikestore_project_dbt_assets
from .project import bikestore_project_project
from .schedules import schedules


DBT_PROJECT_PATH = "I:/Projects/bike_store_project/bikestore_project"
DBT_PROFILES_DIR = "C:/Users/Abo Gouda/.dbt"

defs = Definitions(
    assets=[bikestore_project_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=DBT_PROJECT_PATH,
                              profiles_dir=DBT_PROFILES_DIR)
    },
)


