import speech_recognition as sr


recognizer = sr.Recognizer()

def listen_and_recognize(timeout=None):
    with sr.Microphone() as source:
        print("listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
            print("heard, recognizing")
            text = recognizer.recognize_whisper(audio, model="medium", language='ru')
            print('recognized')
            return text
        except sr.WaitTimeoutError:
            print('waiting')
            return None
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса распознавания; {e}")
        return ""