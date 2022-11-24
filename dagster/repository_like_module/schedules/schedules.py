from dagster import ScheduleDefinition
from ..jobs import jobs

job1_schedule = ScheduleDefinition(job=jobs.job1, cron_schedule="0 0 * * *")