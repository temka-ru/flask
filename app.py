from flask import Flask
# from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_object(Configuration)

# db = SQLAlchemy(app)

# migrate = Migrate(app, db)

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)


app = Flask(__name__)
# app.config.from_object(Configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))