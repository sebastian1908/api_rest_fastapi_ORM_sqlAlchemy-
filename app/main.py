from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
import models,schemas
from Conexion import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return {
        "status": 200,
        "message": "Hola mundo"
    }

@app.get('/productos/{producto_id}',response_model=schemas.Producto)
def get_obtener_users(producto_id:int,db:Session=Depends(get_db)):
    product = db.query(models.Producto).filter_by(id=producto_id).first()
    return product

@app.get('/productos/',response_model=List[schemas.Producto])
def show_producto(db:Session=Depends(get_db)):
    product = db.query(models.Producto).all()
    return product

@app.post('/productos/',response_model=schemas.Respuesta)
def create_productos(entrada:schemas.Producto,db:Session=Depends(get_db)):
    product = models.Producto(nombre_producto = entrada.nombre_producto,precio=entrada.precio,cantidad=entrada.cantidad)
    db.add(product)
    db.commit()
    db.refresh(product)
    respuesta = schemas.Respuesta(status=200,mensaje="Producto agregado con exito")
    return respuesta

@app.put('/productos/{producto_id}',response_model=schemas.Respuesta)
def update_producto(producto_id:int,entrada:schemas.ProducUpdate,db:Session=Depends(get_db)):
    product = db.query(models.Producto).filter_by(id=producto_id).first()
    product.nombre_producto=entrada.nombre_producto
    db.commit()
    db.refresh(product)
    respuesta = schemas.Respuesta(status=200,mensaje="Producto actualizado con exito")
    return respuesta

@app.delete('/productos/{producto_id}',response_model=schemas.Respuesta)
def delete_producto(producto_id:int,db:Session=Depends(get_db)):
    product = db.query(models.Producto).filter_by(id=producto_id).first()
    db.delete(product)
    db.commit()
    respuesta = schemas.Respuesta(status=200,mensaje="Producto Eliminado exitosamente")
    return respuesta