from pathlib import Path

from dagster_dbt import DbtProject

bikestore_project_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "bikestore_project").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
# bikestore_project_project.prepare_if_dev()