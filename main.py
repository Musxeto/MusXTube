# app.py
from flask import Flask, render_template, request, jsonify, Response
from pytube import YouTube
import os
import threading
import time

app = Flask(__name__)

if not os.path.exists('./downloads'):
    os.makedirs('./downloads')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_video_info', methods=['POST'])
def get_video_info():
    try:
        video_url = request.json['videoUrl']
        yt = YouTube(video_url)

        video_info = {
            'title': yt.title,
            'thumbnail': yt.thumbnail_url,
        }

        return jsonify(video_info)
    except Exception as e:
        return jsonify({'error': str(e)})


def download_media(video_url, media_type='video'):
    try:
        yt = YouTube(video_url)

        if media_type == 'video':
            stream = yt.streams.filter(file_extension='mp4', progressive=True).first()
            file_path = f"./downloads/{yt.title.replace(' ', '_')}_progressive.mp4"
        elif media_type == 'audio':
            stream = yt.streams.filter(only_audio=True).first()
            file_path = f"./downloads/{yt.title.replace(' ', '_')}_audio.mp3"
        else:
            return jsonify({'error': 'Invalid media type'})

        if stream:
            stream.download(output_path='./downloads', filename=file_path.split('/')[-1])

        def file_generator(file_path):
            with open(file_path, 'rb') as f:
                while True:
                    chunk = f.read(1024)
                    if not chunk:
                        break
                    yield chunk

        # Start a timer to delete the file after 1 minute
        threading.Timer(20, delete_file, args=[file_path]).start()

        return file_path, file_generator(file_path)
    except Exception as e:
        return jsonify({'error': str(e)})


def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File deleted: {file_path}")
    except Exception as e:
        print(f"Error deleting file: {e}")


@app.route('/download_video', methods=['POST'])
def download_video():
    file_path, file_gen = download_media(request.json['videoUrl'], 'video')
    response = Response(file_gen, mimetype='video/mp4',
                        headers={"Content-Disposition": f"attachment;filename={file_path.split('/')[-1]}"})

    return response


@app.route('/download_audio', methods=['POST'])
def download_audio():
    file_path, file_gen = download_media(request.json['videoUrl'], 'audio')
    response = Response(file_gen, mimetype='audio/mp3',
                        headers={"Content-Disposition": f"attachment;filename={file_path.split('/')[-1]}"})

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
