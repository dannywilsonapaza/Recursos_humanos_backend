from extensions import ma, db
from models import Empleado
from marshmallow import fields, validate


class EmpleadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Empleado
        load_instance = True
        sqla_session = db.session

    # Validaciones adicionales
    idEmpleado = fields.Int(dump_only=True)
    nombre = ma.auto_field(required=True, validate=validate.Length(min=1, max=100))
    departamento = ma.auto_field(required=True, validate=validate.Length(min=1, max=100))
    sueldo = fields.Float(required=True, validate=validate.Range(min=0))


# Instancias para serializar
empleado_schema = EmpleadoSchema()
empleados_schema = EmpleadoSchema(many=True)