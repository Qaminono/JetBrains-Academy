import datetime
from flask import Flask
import sys
from flask_restful import Api, Resource, reqparse, inputs, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy


parser = reqparse.RequestParser()
app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite://events.db'


class Events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()


parser.add_argument(
    'event',
    type=str,
    help='The event name is required!',
    required=True
)

parser.add_argument(
    'date',
    type=inputs.date,
    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
    required=True
)


resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.String,
    'message': fields.String
}


class TodayEventResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Events.query.filter(Events.date == datetime.date.today()).all()


class EventResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Events.query.all()

    @marshal_with(resource_fields)
    def post(self):
        args = parser.parse_args()
        event = Events(event=args.event, date=args.date)
        db.session.add(event)
        db.session.commit()
        return {'message': 'The event has been added!', 'event': args.event, 'date': args.date.strftime('%Y-%m-%d')}


api.add_resource(EventResource, '/event')
api.add_resource(TodayEventResource, '/event/today')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port, debug=True)
    else:
        app.run(debug=True)
