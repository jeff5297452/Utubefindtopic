from flask import Flask, jsonify
import requests
import random
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # ✅ 這行讓回傳的 JSON 用 UTF-8 顯示中文

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
REGION_CODE = 'TW'

@app.route('/trending', methods=['GET'])
def get_trending_video():
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=TW&videoCategoryId=24&key={YOUTUBE_API_KEY}'
    response = requests.get(url)
    data = response.json()

    if 'items' not in data:
        return jsonify({'error': 'API failed', 'details': data}), 500

    video = random.choice(data['items'])
    title = video['snippet']['title']
    video_id = video['id']
    url = f'https://www.youtube.com/watch?v={video_id}'

    return jsonify({'title': title, 'url': url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
