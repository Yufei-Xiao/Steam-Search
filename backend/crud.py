from sqlalchemy.orm import Session
from typing import Tuple, List, Optional
from sqlalchemy import func
from . import models

def search_games(
    db: Session,
    q: str,
    min_price: int,
    max_price: int,
    developer: Optional[str] = None,
    publisher: Optional[str] = None,
    playtime_min: Optional[int] = None,
    playtime_max: Optional[int] = None,
    limit: int = 20,
    offset: int = 0
) -> Tuple[List[models.Game], int]:
    query = db.query(models.Game)
    if q:
        query = query.filter(models.Game.name.ilike(f"%{q}%"))
    query = query.filter(models.Game.price >= min_price, models.Game.price <= max_price)
    if developer:
        query = query.filter(models.Game.developer.ilike(f"%{developer}%"))
    if publisher:
        query = query.filter(models.Game.publisher.ilike(f"%{publisher}%"))
    if playtime_min is not None:
        query = query.filter(models.Game.average_forever >= playtime_min*60)
    if playtime_max is not None:
        query = query.filter(models.Game.average_forever <= playtime_max*60)
    total = query.with_entities(func.count()).scalar() or 0
    results = query.order_by(models.Game.appid.desc()).offset(offset).limit(limit).all()
    return results, int(total)

