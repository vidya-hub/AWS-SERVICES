
import boto3
import os
from pydub import AudioSegment
from pydub.playback import play

client = boto3.client('polly')


def playsound(text):
    res=client.synthesize_speech(Text=text,VoiceId="Matthew",OutputFormat="mp3")
    audio=res["AudioStream"].read()
    speech_file = 'input.mp3'

    with open(speech_file,"wb") as file:
        file.write(audio)
        file.close()
    sound = AudioSegment.from_mp3(speech_file)
    play(sound)
    os.remove(speech_file)
    
playsound("hey sagar how are you")