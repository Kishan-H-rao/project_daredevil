from gtts import gTTS
import pygame

text = "Hello, world! how are you , when will you come home"
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
