import os
from dotenv import load_dotenv

load_dotenv() 

AIRBYTE_CONFIG = {
	"host": os.environ.get("MY_AIRBYTE_HOST"),
	"port": os.environ.get("MY_AIRBYTE_PORT")
}

DBT_CONFIG = {
	"host": os.environ.get("MY_DBT_HOST"),
	"port": int(os.environ.get("MY_DBT_HOST_PORT"))
}
