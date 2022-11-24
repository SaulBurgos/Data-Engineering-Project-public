import sys
from fastapi import FastAPI, Depends
import requests
import json
from .schemas import UserBase
from sqlalchemy.orm import Session
from .database import get_db
from .model import User

app = FastAPI()

@app.get("/")
def read_root(db: Session = Depends(get_db)):

    airbyte_response = requests.get('http://airbyte-webapp/api/v1/health/')

    dagster_response = requests.post(
        "http://docker_example_dagit:3000/graphql", 
        json={'query':'{version}'}
    )

    status_req = {
        "jsonrpc": "2.0",
        "method": "status",
        "id": "2db9a2fe-9a39-41ef-828c-25e04dd6b074"
    }

    dbt_response = requests.post(
        'http://docker_example_dbt:8580/jsonrpc', 
        json.dumps(status_req)
    )

    users = get_users(
        db=db
    )
    
    return {
        "airbyte": airbyte_response.json(),
        "dagster": dagster_response.json(),
        "dbt": dbt_response.json(),
        "usersDatabase": users
    }

def get_users(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(User).offset(skip).limit(limit).all()
    except Exception as error:
        print(error,file=sys.stderr)