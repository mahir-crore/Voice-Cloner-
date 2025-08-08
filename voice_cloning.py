from TTS.api import TTS
from io import BytesIO
import soundfile as sf
audio_path="/content/virat kohli.mp3"
text= "hello sir may i help you please  tell  me  i will help you "
def clone_voice( text=text, speed = 1.5) -> BytesIO:
    print("Loading TTS model...")
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)
    
    print("Cloning voice...")
    audio_array = tts.tts(
        text=text,
        speaker_wav=audio_path,
        language="en",
        speed=speed
    )
    
    audio_buffer = BytesIO()
    sf.write(audio_buffer, audio_array, 22050, format='WAV')
    audio_buffer.seek(0)
    
    print("Voice cloned and saved to memory.")
    return audio_buffer
