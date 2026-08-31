from sqlalchemy import Column, Integer, String, Text, DateTime, func
from database import Base


class Incidencia(Base):
    __tablename__ = "incidencias"

    id = Column(Integer, primary_key=True, index=True)
    pedido = Column(String, index=True, nullable=True)       # numero de venta / orden VTEX
    sucursal = Column(String, nullable=True)
    descripcion = Column(Text, nullable=False)
    estatus = Column(String, default="abierta")               # abierta / en_proceso / resuelta
    reportado_por = Column(String, nullable=True)
    creado_en = Column(DateTime(timezone=True), server_default=func.now())
    actualizado_en = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
