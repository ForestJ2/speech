import subprocess
import speech_recognition as sr


def get(phrase_time=5, timeout=30, debug=False):
    r = sr.Recognizer()
    value = ''

    with sr.Microphone() as source:
        if debug: print "[DEBUG] adjusting for ambient noise..."
        r.adjust_for_ambient_noise(source, duration=0.7)

        try: audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time)  # if a lot of sound is around, this will keep it from waiting forever.
        except sr.WaitTimeoutError: return False

    try:
        value = r.recognize_google(audio).lower()
        if debug: print "\n[DEBUG] Command: " + value

        return value

    except sr.UnknownValueError: return False
    except sr.RequestError as e:
        if debug: print "[DEBUG] google error: {0}".format(e)
        return False
    except KeyError as e:
        # only error so far is `missing key: confidence`, meaning it didn't know what was said
        if debug: print "[DEBUG] key error: {0}".format(e)
        return False


def say(value, debug=False):
    if str(type(value)) not in ["<type 'str'>", "<type 'unicode' >"]:
        raise TypeError("stt.say argument 'value' only accepts string/unicode types")

    if debug is True:
        print "[DEBUG] stt.say received speak value '{0}'".format(value)

    proc = subprocess.Popen(["tts.exe", value],
                            shell=False,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    out, error = proc.communicate()

    if len(error) > 0 and debug is True:
        print "[DEBUG] stt.say error: " + error
