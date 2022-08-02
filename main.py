from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# need to instantiate a flask app
app = Flask(__name__)
# instantiate api
api = Api(app)

names = {"Rohit": {"age": 18, "gender": "male"},
         "Tim": {"age": 19, "gender": "male"}}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=str, help="Views on the video is required", required=True)
video_put_args.add_argument("likes", type=str, help="Likes on the video is required", required=True)
# create resource
videos = {}


class Video(Resource):
    # handling errors: create abort functions at the top and then call them at the beginning of every method
    def abort_invalid_id(self, video_id):
        if video_id not in videos:
            abort(404, message="Couldn't find video")

    def abort_id_exists(self, video_id):
        if video_id in videos:
            abort(409, message="Video already exists with that id")

    def get(self, video_id):
        self.abort_invalid_id(video_id)
        return videos[video_id]

    def post(self, video_id):
        self.abort_id_exists(video_id)
        # reason we're using request parser: automatically sends back an error message if some argument is missing
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        self.abort_invalid_id(video_id)
        del videos[video_id]
        # usually with delete requests, we send an empty message
        return '', 204


# all resources need to be registered in order to connect class to API
# can pass in an optional argument here that can be accessed throughout the entire class
api.add_resource(Video, "/video/<int:video_id>")
# format: class name, path

# run app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
