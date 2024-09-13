from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base): 
    __tablename__ = 'usuario'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nomre=Column(String(50))
    correo=Column(String(20))
    contraseña=Column(String(10))
    ciudad=Column(Integer(50)) 
    telefono=Column(Integer(11))

class Gasto(Base):
    __tablename__ = 'gasto'
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(250))
    nombre=(String(50))

class Categoría(Base):
    __tablename__ = 'categoria'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    fotoicono=Column(String(50))

class ingreso(Base):
    __tablename__ = 'ingreso'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    valor=Column(Integer(50))
    descripcion=Column(String(250))

class transaccion(Base):
    __tablename__ = 'transaccion'
    id=Column(Integer, primary_key=True, autoincrement=True)
    numeroTransaccion=Column(Integer(20))
    valor=Column(Integer(50))
    descripcion=Column(String(250))

