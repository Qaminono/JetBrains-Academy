import datetime
from flask import Flask, abort
import sys
from flask_restful import Api, Resource, reqparse, inputs, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy


parser = reqparse.RequestParser()

parser.add_argument(
    'event',
    type=str,
    help='The event name is required!',
    required=True)

parser.add_argument(
    'date',
    type=inputs.date,
    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
    required=True)

time_parser = reqparse.RequestParser()

time_parser.add_argument(
    'start_time',
    type=inputs.date,
    help='The start date with the correct format is required! The correct format is YYYY-MM-DD!')

time_parser.add_argument(
    'end_time',
    type=inputs.date,
    help='The end date with the correct format is required! The correct format is YYYY-MM-DD!')


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite://events.db'


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()

resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.String
}


class TodayEventResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Event.query.filter(Event.date == datetime.date.today()).all()


class EventResource(Resource):
    @marshal_with(resource_fields)
    def get(self):
        args = time_parser.parse_args()
        if args.start_time and args.end_time:
            return Event.query.filter(Event.date.between(args.start_time, args.end_time)).all()
        return Event.query.all()

    def post(self):
        args = parser.parse_args()
        event = Event(event=args.event, date=args.date)
        db.session.add(event)
        db.session.commit()
        return {'message': 'The event has been added!', 'event': args.event, 'date': args.date.strftime('%Y-%m-%d')}


class EventByID(Resource):
    @marshal_with(resource_fields)
    def get(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        return event

    def delete(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        db.session.delete(event)
        db.session.commit()
        return {"message": "The event has been deleted!"}


api.add_resource(EventResource, '/event')
api.add_resource(TodayEventResource, '/event/today')
api.add_resource(EventByID, '/event/<int:event_id>')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port, debug=True)
    else:
        app.run(debug=True)