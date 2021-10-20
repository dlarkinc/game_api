from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class SaveHighScore(Resource):
    def get(self, sid, time):
        return {'sid': sid, 'time': time}

api.add_resource(SaveHighScore, '/id/<string:sid>/time/<float:time>')

if __name__ == '__main__':
    app.run(debug=True)