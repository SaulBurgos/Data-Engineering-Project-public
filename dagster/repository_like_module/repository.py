from dagster import repository, job
from .assets import assets
from .jobs import jobs
from .schedules import schedules
from .sensors import sensors
from .ops import ops
from dagster_dbt import dbt_run_op


@job(resource_defs={"airbyte": ops.my_airbyte_resource})
def my_simple_airbyte_job():
    ops.sync_foobar()
	
@job(resource_defs={
    "dbt": ops.custom_dbt_rpc_resource
})
def my_dbt_rpc_job():
    dbt_run_op()

@job(resource_defs={
    "dbt": ops.custom_dbt_rpc_resource,
    "airbyte": ops.my_airbyte_resource
})
def dependencies_airbyte_dbt():
    dbt_run_op(
        ops.sync_foobar()
    )


@repository
def repository_like_module():
	return [
			assets.asset1,
			assets.asset2,
			assets.asset3,
			schedules.job1_schedule,
			sensors.job2_sensor,
			jobs.job3,
			my_simple_airbyte_job,
            my_dbt_rpc_job,
            dependencies_airbyte_dbt
	]