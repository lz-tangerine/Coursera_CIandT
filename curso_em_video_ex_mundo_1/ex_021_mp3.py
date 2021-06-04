from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("/home/carolinam/Downloads/sound.mp3")
play(song)
