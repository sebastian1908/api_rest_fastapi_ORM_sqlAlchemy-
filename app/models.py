from sqlalchemy import Column, Integer, String
from Conexion import Base

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer,primary_key=True,index=True)
    nombre_producto = Column(String(20))
    precio = Column(Integer)
    cantidad = Column(Integer)

