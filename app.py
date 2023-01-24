import json
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import requests

# app = Flask(__name__, static_folder="./build/", static_url_path="/")

app = Flask(__name__)
twitter_api = Api(app)

params = {'q': 'nasa', 'result_type': 'popular'}
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAKEqlAEAAAAAY3hQj7IzoFuacC7s%2FdQy1bRFU3c%3DknJZmbrFQSh7CEr9r6dZeJ6LdREU3b4jFXfEGAueadLUX3e6YB' }
twitter_search_url="https://api.twitter.com/1.1/search/tweets.json";

twitter_request = requests.get(twitter_search_url, headers=headers, params=params)
print(twitter_request.text)


@app.route('/get_tweet_by_username/<twitter_user>', methods=['GET'])
def get_tweet(twitter_user):


    return "You just searched for {0}".format(twitter_user)



twitter_api.add_resource("https://api.twitter.com/2/tweets/search/recent?query=from:twitterdev")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
else:
    app.run(debug=True)