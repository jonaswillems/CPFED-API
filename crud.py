#Created by Jonas Willems.
#!/usr/bin/env python3


from sqlalchemy.orm import Session

import models
import schemas

def get_values(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.API).offset(skip).limit(limit).all()

def get_value(db: Session, Id: int):
    return db.query(models.API).filter(models.API.Id == Id).first()

def create_value(db: Session, API: schemas.APICreate):
    db_item = models.API(**API.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

