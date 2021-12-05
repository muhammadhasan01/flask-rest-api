from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
    "hasan": {
        "age": 21,
        "gender": "male"
    },
    "fulanah": {
        "age": 25,
        "gender": "female"
    }
}

videos = {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        print(request.form)
        return {}


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
