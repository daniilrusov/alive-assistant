from llm import get_response, add_to_history
from tts import tts_text
from stt import listen_and_recognize


history = []

print("Скажите 'живой', чтобы начать запись.")

while True:
    text = listen_and_recognize(timeout=1)

    if text:
        print(text)

        if "стоп" in text.lower():
            print("стоп")
            history = []
            continue

        if "живой" in text.lower():
            print("Распознан триггер 'живой'. Отправляю текст в модель.")
            history = add_to_history(history, text[6:], "user")
            response = get_response(history)
            first = response.split('.')[0]
            history = add_to_history(history, first, "assistant")
            tts_text(first)
            continue
