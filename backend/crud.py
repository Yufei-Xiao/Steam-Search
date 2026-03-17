from sqlalchemy.orm import Session
from typing import Tuple, List, Optional
from sqlalchemy import func
from . import models

def search_games(db:Session,q:str,min_price:int,max_price:int,limit:int=20,offset:int=0)->Tuple[List[models.Game],int]:
    query=db.query(models.Game)
    if q:
        query=query.filter(models.Game.name.ilike(f"%{q}%"))
    query=query.filter(models.Game.price>=min_price,models.Game.price<=max_price)
    total = query.with_entities(func.count()).scalar() or 0
    results = query.order_by(models.Game.appid.desc()).offset(offset).limit(limit).all()
    return results, int(total)

