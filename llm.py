import ollama


def add_to_history(history, text, role):
    if len(history) == 0:
        history = [
            {"role": "system", "content": "Твое имя Живой, ты мой личный помощник. Отвечай только на русском максимум в два предложения."}
            ]
    history.append({"role": role, "content": text})
    return history

def get_response(history):
    response = ollama.chat(
        model="phi3",
        messages=history
    )
    text = response['message']['content']
    return text
