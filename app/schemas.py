from typing import Optional
from pydantic import BaseModel

class Producto(BaseModel):
    id:Optional[int]
    nombre_producto:str
    precio:int
    cantidad:int

    class Config:
        orm_mode =True

class ProducUpdate(BaseModel):   
    nombre_producto:str

    class Config:
        orm_mode =True
        

class Respuesta(BaseModel):   
    status: int
    mensaje:str

class leerInfoUsuario(BaseModel):   
    id:int


   