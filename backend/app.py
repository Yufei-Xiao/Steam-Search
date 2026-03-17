from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import backend.db as db
import backend.crud as crud
import backend.schemas as schemas
from typing import Optional

app = FastAPI(title="Steam Search")
origins=["http://127.0.0.1:5500"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    db.Base.metadata.create_all(bind=db.engine)


@app.get("/get/games", response_model=schemas.GameSearchResults)
def api_search_games(q: Optional[str] = "", limit: int = 20, offset: int = 0, min_price : int = 0, max_price : int = 999999, session: Session = Depends(db.get_db)):
    results, total =crud.search_games(session,q or "", min_price, max_price, limit=limit, offset=offset)
    return {"results": results, "total": total}