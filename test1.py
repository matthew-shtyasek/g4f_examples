import g4f

messages = [{'role': 'system', 'content': '''GPT, ты являешься Альбертом Эйнштейном. Обладая исчерпывающими познаниями в области
             общей и специальной теорий относительности, ты так же умеешь их объяснять не только при помощи формул, но и при помощи
             базовых концепций на интуитивном уровне.'''}]
while True:
    msg = input()
    
    if msg == 'end':
        break

    messages += [{'role': 'user', 'content': msg}]

    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4_32k,
        messages=messages,
        stream=True
    )

    message = ''
    for token in response:
        message += token
        print(token, flush=True, end='')

    messages += [{'role': 'assistant', 'content': message}]
