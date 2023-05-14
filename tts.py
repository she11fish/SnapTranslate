import requests
import json
import requests
import requests
import vlc
import time

def play_audio(audio_url):
    content = requests.get(audio_url).content
    with open("sound.wav", mode="wb") as f:
        f.write(content)
    filename = 'sound.wav'
    player = vlc.MediaPlayer(filename)
    player.audio_set_volume(100)
    player.play() 
    time.sleep(0.1)
    while player.is_playing():
        pass
    time.sleep(3)

def text_to_speech(text, langauge):
    if langauge == "ar":
        voice_id =  700542
    if langauge == "en":
        voice_id = 148
    if langauge == "fr":
        voice_id = 257
    url = 'https://api.ttsmaker.com/v1/create-tts-order'
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    params = {
        'token': 'ttsmaker_demo_token',
        'text': text,
        'voice_id': voice_id,
        'audio_format': 'wav',
        'audio_speed': 1.0,
        'audio_volume': 0,
        'language': "ar",
        'text_paragraph_pause_time': 0
    }
    response = requests.post(url, headers=headers, data=json.dumps(params))
    data = response.json()
    stream_url = data['audio_file_url']
    play_audio(stream_url)