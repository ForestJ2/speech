# speech

> Python functions that wrap the speech_recognition library. Making recognizing spoken speech a 1 line process.

## DEPENDENCIES

speech_recognition (pip)

tts.exe, or any TTS program that takes an argument and converts it to computer spoken audio.

## USAGE

### Obtaining Speech

```python
import speech

print speech.get()
```

### TTS

```python
import speech

speech.say("Hello world!")
```
