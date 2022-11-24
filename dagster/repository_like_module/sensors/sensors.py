from dagster import RunRequest, sensor
from ..jobs import jobs

@sensor(job=jobs.job2)
def job2_sensor():
	should_run = True
	if should_run:
			yield RunRequest(run_key=None, run_config={})