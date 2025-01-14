from config import *
from typing import List
from model.tools.Jsonifyer import *
from sqlalchemy import or_, and_

class BaseData(Jsonifyer):
    id = db.Column(db.Integer, primary_key=True)
    
    def __init__(self, id = None):
        Jsonifyer.__init__(self)
        if id != None:
            self.id = id
            
    def save(self):
        db.session.add(self)
        db.session.commit()
        
   
    @classmethod 
    def getAll(cls) -> List["BaseData"]:
        return cls.query.all()
    
    @classmethod 
    def getByID(cls, searchId:int) -> "BaseData":
        return cls.query.filter_by(id=searchId).first()
    
    @classmethod
    def getLast(cls):
        return cls.query.order_by(cls.id.desc()).first()
    
    @classmethod
    def getLastList(cls, count=None):
        if count is None:
            return cls.query.order_by(cls.id.desc()).limit(count)
        return cls.query.order_by(cls.id.desc()).all()

    def delete(self):
        print(f'deleting {self}')
        db.session.delete(self)
        db.session.commit()
    
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.getParamsList()}>"
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.getParamsList()}"
    
    
    
        
    