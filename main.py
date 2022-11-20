#Created by Jonas Willems.
#CPFED-API: Cheapest Price For Energy Drinks API
#!/usr/bin/env python3


from fastapi import Depends, FastAPI, HTTPException
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
import crud
import models
import schemas
import os
import json

app = FastAPI()

origins = [
    "http://127.0.0.1:8080/",
    "http://127.0.0.1:8000/"
    "http://127.0.0.1:8000/get/drankje"
    "http://127.0.0.1:8000/get/drankjes"
    "http://127.0.0.1:8000/get/values/"
    "http://127.0.0.1:8000/get/value/"
    "http://127.0.0.1:8000/post/drankje/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get/drankjes/", response_model=list[schemas.APIBase])
def get_stores(db: Session = Depends(get_db)):
    values = crud.get_values(db)
    if values is None:
        raise HTTPException(status_code=404, detail="Geen drankjes gevonden!")
    return values

@app.get("/get/drankje/{Id}", response_model=schemas.APIBase)
def get_store(Id: int, db: Session = Depends(get_db)):
    db_api = crud.get_value(db, Id=Id)
    if db_api is None:
        raise HTTPException(status_code=404, detail="Winkel niet gevonden!")
    return db_api   

@app.post("/post/drankje/", response_model=schemas.APICreate)
def add_store(API: schemas.APIBase, db: Session = Depends(get_db)):
        if db_api is None:
            raise HTTPException(status_code=404, detail="Winkel niet gevonden!")
        return crud.create_value(db=db, API=API)