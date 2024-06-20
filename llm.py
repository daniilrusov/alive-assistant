import ollama

def get_response(text):
    response = ollama.chat(
        model="phi3",
        messages=[
            {"role": "system", "content": "Твое имя Живой, ты мой личный помощник. Отвечай только на русском максимум в два предложения."},
            {"role": "user", "content": text }
        ]
    )
    text = response['message']['content']
    return text
