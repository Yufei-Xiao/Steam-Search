from sqlalchemy.orm import Session
from typing import Tuple, List, Optional
from sqlalchemy import func
from . import models

def search_games_by_name(db:Session,q:str,limit:int=20,offset:int=0)->Tuple[List[models.Game],int]:
    pattern = f"%{q}%"
    query = db.query(models.Game).filter(models.Game.name.ilike(pattern))
    total = query.with_entities(func.count()).scalar() or 0
    results = query.order_by(models.Game.appid.desc()).offset(offset).limit(limit).all()
    return results, int(total)

