# app/tts_engine.py
from TTS.api import TTS

# Use a natural sounding model (offline)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
print("###################### NO CRASH ####################")
def generate_audio(text, output_path="output.wav"):
    tts.tts_to_file(text=text, file_path=output_path)