import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig

def speak(a):
	#Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal
	#Remember to delete the brackets <> when pasting your key and region!
    speech_config = speechsdk.SpeechConfig(subscription="5ae338b9cfeb46a8b4b5e5efbf9dede7", region="centralindia")
    speech_config.speech_synthesis_voice_name ="en-US-ChristopherNeural"
    audio_config = AudioOutputConfig(use_default_speaker=True)
    # audio_config = AudioOutputConfig(filename="hello.wav")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(a)
