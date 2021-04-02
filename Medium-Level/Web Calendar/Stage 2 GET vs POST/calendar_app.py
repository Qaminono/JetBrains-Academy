from flask import Flask
import sys
from flask_restful import Api, Resource, reqparse, inputs


parser = reqparse.RequestParser()
app = Flask(__name__)
api = Api(app)

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


class EventResource(Resource):
    def post(self):
        args = parser.parse_args()
        return {'message': 'The event has been added!', 'event': args.event, 'date': args.date.strftime('%Y-%m-%d')}


api.add_resource(EventResource, '/event')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port, debug=True)
    else:
        app.run(debug=True)
