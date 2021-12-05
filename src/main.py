from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes}"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Number of likes on the video", required=True)

videos = {}


def handle_non_existing_video(video_id):
    if video_id not in videos:
        abort(404, message="Video id = {} is not in the data".format(video_id))


def handle_existing_video(video_id):
    if video_id in videos:
        abort(409, message="Video id = {} already exist".format(video_id))


class Video(Resource):
    def get(self, video_id):
        handle_non_existing_video(video_id)
        return videos[video_id]

    def put(self, video_id):
        handle_existing_video(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        handle_non_existing_video(video_id)
        del videos[video_id]
        return "".format(video_id), 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
