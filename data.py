import openai


def check(name):
    openai.api_key = "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"
    model_engine = "text-davinci-003"
    prompt = f"Has {name} played for Barcelona"
    # задаем макс кол-во слов
    max_tokens = 1
    # генерируем ответ
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # выводим ответ
    result_row = completion.choices[0].text
    print(result_row)
    prompt = f"Has {name} played for Spain "
    # задаем макс кол-во слов
    max_tokens = 1
    # генерируем ответ
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # выводим ответ
    result_column = completion.choices[0].text
    if "Yes" in result_column and "Yes" in result_row:
        return True
    else:
        return False

print(check('Kepa'))
