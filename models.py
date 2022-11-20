#Created by Jonas Willems.
#!/usr/bin/env python3


from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

class API(Base):
    __tablename__ = "info"
    Id = Column(Integer, primary_key=True, index=True)
    storeName = Column(String, index=True)
    drinkName = Column(String, index=True)
    drinkPrice = Column(Float, index=True)