# Real-Time-Voice-to-Voice-AI-Translator
Real-Time Voice to Voice AI Translator
This project is a Real-Time Voice to Voice AI Translator built with Python, Gradio, AssemblyAI, ElevenLabs, and the translate library. It allows users to speak into their microphone, transcribes their speech to text, translates the text into Spanish, French, and Japanese, and then converts the translated text back into speech in each target language. The result is a seamless, interactive, multilingual voice translation experience.

Features
Real-time Speech Recognition: Converts spoken audio to text using AssemblyAI.

Multilingual Translation: Translates English speech into Spanish, French, and Japanese.

Natural Voice Synthesis: Uses ElevenLabs to generate high-quality speech in each target language.

User-Friendly Interface: Gradio provides a simple web interface for recording and playback.

Setup Instructions
1. Clone the Repository
bash
git clone https://github.com/yourusername/voice-to-voice-translator.git
cd voice-to-voice-translator
2. Install Dependencies
bash
pip install gradio assemblyai python-dotenv elevenlabs translate
3. Obtain API Keys
AssemblyAI: Sign up and get your API key

ElevenLabs: Sign up and get your API key

4. Configure Environment Variables
Create a .env file in the project root:

text
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
Note: In the provided code, API keys are hardcoded. For production use, replace them with os.getenv("ASSEMBLYAI_API_KEY") and os.getenv("ELEVENLABS_API_KEY") for improved security.

5. Run the App
bash
python app.py
The Gradio interface will launch in your browser. Click the microphone to record, and listen to your translations in Spanish, French, and Japanese.

File Structure
text
voice-to-voice-translator/

│

├── app.py          # Main application script

├── .env            # Environment variables (not included in repo)

├── requirements.txt

└── README.md

Acknowledgements
AssemblyAI for speech-to-text

ElevenLabs for text-to-speech

Gradio for the web interface

translate Python library

License
MIT License
