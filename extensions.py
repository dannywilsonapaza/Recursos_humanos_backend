from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Inicialización de extensiones
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

"""
Por qué se hace así:
- Separar las extensiones en este archivo evita importaciones circulares
- Permite inicializar las extensiones una vez y importarlas donde se necesiten
- Facilita el mantenimiento y la escalabilidad
"""