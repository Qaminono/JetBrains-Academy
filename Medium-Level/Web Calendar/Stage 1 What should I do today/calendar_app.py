from flask import Flask
import sys
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class EventResource(Resource):
    def get(self):
        return {"data": "There are no events for today!"}


api.add_resource(EventResource, '/event/today')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port, debug=True)
    else:
        app.run(debug=True)
