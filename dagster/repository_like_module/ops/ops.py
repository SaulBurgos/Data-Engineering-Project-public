from dagster import op
from dagster_airbyte import airbyte_resource, airbyte_sync_op
from ..shared import constants
from dagster_dbt import dbt_rpc_sync_resource

@op
def hello():
	pass

my_airbyte_resource = airbyte_resource.configured(constants.AIRBYTE_CONFIG)
sync_foobar = airbyte_sync_op.configured({"connection_id": "01eb3f35-ed95-4333-99fe-f64ac8c85023"}, name="sync_foobar")

custom_dbt_rpc_resource = dbt_rpc_sync_resource.configured(
	constants.DBT_CONFIG
)