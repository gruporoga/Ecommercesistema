from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Incidencia

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Control Roga API")


class IncidenciaIn(BaseModel):
    pedido: Optional[str] = None
    sucursal: Optional[str] = None
    descripcion: str
    reportado_por: Optional[str] = None


class IncidenciaUpdate(BaseModel):
    estatus: str


class IncidenciaOut(IncidenciaIn):
    id: int
    estatus: str

    class Config:
        from_attributes = True


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/incidencias", response_model=List[IncidenciaOut])
def listar_incidencias(db: Session = Depends(get_db)):
    return db.query(Incidencia).order_by(Incidencia.creado_en.desc()).all()


@app.post("/incidencias", response_model=IncidenciaOut)
def crear_incidencia(payload: IncidenciaIn, db: Session = Depends(get_db)):
    inc = Incidencia(**payload.model_dump())
    db.add(inc)
    db.commit()
    db.refresh(inc)
    return inc


@app.patch("/incidencias/{incidencia_id}", response_model=IncidenciaOut)
def actualizar_estatus(incidencia_id: int, payload: IncidenciaUpdate, db: Session = Depends(get_db)):
    inc = db.query(Incidencia).filter(Incidencia.id == incidencia_id).first()
    if not inc:
        raise HTTPException(status_code=404, detail="No encontrada")
    inc.estatus = payload.estatus
    db.commit()
    db.refresh(inc)
    return inc
