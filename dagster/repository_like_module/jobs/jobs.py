from dagster import  job
from ..ops import ops

@job
def job1():
	ops.hello()

@job
def job2():
	ops.hello()

@job
def job3():
	ops.hello()
