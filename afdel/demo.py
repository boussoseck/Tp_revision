from transformers import pipeline
import librosa
from noisereduce import reduce_noise
import gradio as gr

def transc_pipeline ()-> str :
    y,sr = librosa.load(audio, sr = 16000)
    noise_reduced = reduce_noise(y=y, sr=sr)
    pipe = pipeline('automatic-speech-recognition', model = 'serge-wilson/wav2vec-base-wolof')
    transcription = pipe("audio/WOL_05_lect_0027.wav")

    return transcription

gr.Interface(
    fn
)
