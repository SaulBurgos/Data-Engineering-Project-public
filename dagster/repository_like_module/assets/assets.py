from dagster import asset

@asset
def asset1():
	pass

@asset
def asset2():
	pass

@asset(group_name="mygroup")
def asset3():
	pass
