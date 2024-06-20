import pyaudio
import speech_recognition as sr
import time

from llm import get_response
from tts import tts_text



# Инициализация распознавателя
recognizer = sr.Recognizer()


# Функция для прослушивания микрофона и распознавания речи
def listen_and_recognize(timeout=None):
    with sr.Microphone() as source:
        print("Слушаю...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
            print(audio)
            text = recognizer.recognize_whisper(audio, model="medium", language='ru')
            print('processed')
            return text
        except sr.WaitTimeoutError:
            print('waiting')
            return None
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f"Ошибка сервиса распознавания; {e}")
        return ""

# Основной цикл прослушивания
print("Скажите 'живой', чтобы начать запись.")
recording = False
captured_text = []
last_spoken_time = None
silence_threshold = 3  # секунды

while True:
    text = listen_and_recognize(timeout=1)
    current_time = time.time()

    if text:
        last_spoken_time = current_time
        print(text)

        if "живой" in text.lower():
            print("Распознан триггер 'живой'. Отправляю текст в модель.")
            response = get_response(text[6:])
            tts_text(response)
            continue
