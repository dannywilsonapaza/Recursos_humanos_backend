# python
from sqlalchemy import Numeric
from extensions import db


class Empleado(db.Model):
    """
       Modelo de datos para la tabla empleados
       Representa la estructura de la tabla en la base de datos
       """
    __tablename__ = 'empleados'

    idEmpleado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100), nullable=False)
    sueldo = db.Column(Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"<Empleado id={self.idEmpleado} nombre={self.nombre}>"
