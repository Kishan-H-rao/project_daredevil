# Install the assemblyai package by executing the command `pip3 install assemblyai` (macOS) or `pip install assemblyai` (Windows).

# Import the AssemblyAI module
import assemblyai as aai
import main
# Your API token is already set here
aai.settings.api_key = "7dcb1567b0654956bad4d4273b6358d2"

# Create a transcriber object.
transcriber = aai.Transcriber()

# If you have a local audio file, you can transcribe it using the code below.
# Make sure to replace the filename with the path to your local audio file.
# transcript = transcriber.transcribe("./my-local-audio-file.wav")
# 
# Alternatively, if you have a URL to an audio file, you can transcribe it with the following code.
# Uncomment the line below and replace the URL with the link to your audio file.
transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/espn-bears.m4a")
# assemblyai transcribe "https://youtu.be/0wvBu014E5o" --auto_highlights --entity_detection
# After the transcription is complete, the text is printed out to the console.
print(main.textToAudio(transcript.text))