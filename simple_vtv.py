import gradio as gr
import assemblyai as aai
from translate import Translator
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import uuid
from pathlib import Path
from dotenv import load_dotenv
import os  

# Load environment variables from .env file
load_dotenv()

# # Load AssemblyAI and ElevenLabs API keys
# aai.settings.api_key = "ASSEMBLYAI_API_KEY" # your assemblyai api key
# Load ElevenLabs API key   
# elevenlabs_api_key = "ELEVENLABS_API_KEY" # your elevenlabs api key

def voice_to_voice(audio_file):
    
    #transcribe audio
    transcription_response = audio_transcription(audio_file)

    if transcription_response.status == aai.TranscriptStatus.error:
        raise gr.Error(transcription_response.error)
    else:
        text = transcription_response.text

    es_translation, fr_translation, ja_translation = text_translation(text)

    es_audi_path = text_to_speech(es_translation)
    fr_audi_path = text_to_speech(fr_translation)
    ja_audi_path = text_to_speech(ja_translation)

    es_path = Path(es_audi_path)
    fr_path = Path(fr_audi_path)
    ja_path = Path(ja_audi_path)

    return es_path, fr_path, ja_path


def audio_transcription(audio_file):

    aai.settings.api_key = "<your assemblyai API key>" # your assemblyai api key

    transcriber = aai.Transcriber()
    transcription = transcriber.transcribe(audio_file)

    return transcription

def text_translation(text):
    
    translator_es = Translator(from_lang="en", to_lang="es")
    es_text = translator_es.translate(text)

    translator_fr = Translator(from_lang="en", to_lang="fr")
    fr_text = translator_fr.translate(text)

    translator_ja = Translator(from_lang="en", to_lang="ja")
    ja_text = translator_ja.translate(text)

    return es_text, fr_text, ja_text

def text_to_speech(text):

    client = ElevenLabs(
        api_key= "<your elevenlabs API key>", # your elevenlabs api key
    )

    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="<Your voice id>", #clone your voice on elevenlabs dashboard and copy the id
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.8,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"{uuid.uuid4()}.mp3"

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file
    return save_file_path

audio_input = gr.Audio(
    sources=["microphone"],
    type="filepath"
)

demo = gr.Interface(
    fn=voice_to_voice,
    inputs=audio_input,
    outputs=[gr.Audio(label="Spanish"), gr.Audio(label="French"), gr.Audio(label="Japanese")]
)

if __name__ == "__main__":
    demo.launch()
