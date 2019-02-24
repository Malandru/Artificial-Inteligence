from watson_developer_cloud import SpeechToTextV1
from os.path import join, dirname
import json

speech_to_text = SpeechToTextV1(
    username='1cdeee9b-c19f-4f56-86e7-f2eabe9bddc6',
    password='Sha6pvxvR3Yu',
    url='https://stream.watsonplatform.net/speech-to-text/api'
)

file = 'audio-file.flac'
with open(join(dirname(__file__), './.', file),
                   'rb') as audio_file:
        results = speech_to_text.recognize(
            audio=audio_file,
            content_type='audio/flac',
        ).get_result()
        
print(json.dumps(results, indent=2))