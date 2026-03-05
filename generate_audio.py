"""Two Truths and One Lie - ElevenLabs TTS 오디오 생성"""
import os
from elevenlabs import ElevenLabs, VoiceSettings

api_key = os.environ["ELEVENLABS_API_KEY"]
client = ElevenLabs(api_key=api_key)

VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # Adam - clear English male voice
MODEL_ID = "eleven_v3"

statements = {
    "q1a": "I prepare for class using a braille textbook.",
    "q1b": "I majored in math in college.",
    "q1c": "I have been teaching English since 2010.",
    "q2a": "My computer reads the text on the screen out loud for me.",
    "q2b": "I have been working at Sinmyeong Middle School for five years.",
    "q2c": "I studied abroad in England for one year.",
    "q3a": "I read documents by touching braille with my fingertips.",
    "q3b": "I only teach first grade English this year.",
    "q3c": "I have also taught Japanese before.",
}

output_dir = os.path.join(os.path.dirname(__file__), "audio")
os.makedirs(output_dir, exist_ok=True)

for name, text in statements.items():
    output_path = os.path.join(output_dir, f"{name}.mp3")
    if os.path.exists(output_path):
        print(f"  skip {name} (already exists)")
        continue
    print(f"  generating {name}: {text}")
    audio_gen = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        model_id=MODEL_ID,
        text=text,
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.75,
            style=0.0,
            use_speaker_boost=True,
            speed=0.9,
        ),
    )
    audio_data = b"".join(audio_gen)
    with open(output_path, "wb") as f:
        f.write(audio_data)
    print(f"  saved {output_path} ({len(audio_data)/1024:.1f} KB)")

print("\nDone!")
