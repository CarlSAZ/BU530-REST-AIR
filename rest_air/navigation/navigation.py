""" from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from marshmallow import Schema, fields
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

def create_app(config_filename):
    '''Standard Flask API factory pattern'''
    app = Flask(__name__)
    #Optional ability to feed configuration via config file...
    #app.config.from_pyfile(config_filename)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///navigation.db"
    api = Api(app)
    api.add_resource(Journey,"/navigation/journey/<input0>")
    api.add_resource(DirectionList,"/navigation/direction/")
    api.add_resource(Direction,"/navigation/direction/<input0>")
    api.init_app(app)
    
    with app.app_context():
        db.create_all()
    return app

class DirectionModel(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)

class JourneyModel(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)


def abort_if_step_not_found(step_id):
    if step_id not in direction_steps:
        abort(404,message="Direction Step {} doesn't exist".format(step_id))

class Journey(Resource):
    def get(self):
        pass

    def put(self):
        pass
    
    def post(self):
        pass

    def delete(self):
        """Stops the journey and deletes it"""
        pass

direction_steps = []

class DirectionStepSchema(Schema):
    direction= fields.Str(required=True)
    distance = fields.Float(required=True)
    create_at = fields.DateTime()

class Direction(Resource):
    
    def get(self, step_id):
        abort_if_step_not_found(step_id)
        return direction_steps[step_id]
    
    def post(self,step_id):
        pass

class DirectionList(Resource):
    def get(self):
        return direction_steps
 """