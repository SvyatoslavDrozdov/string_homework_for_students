"""
Вам дан список предложений.
Предложения содержит только слова, которые разделены единичными пробелами.
Необходимо вернуть максимальное количество слов, которое содержится в одном предложении.
sentences[i] - это одно предложение.
Если ни одно из предложений не содержит слов, то нужно вернуть 0
Проверка:
pytest ./3_maximum_number_of_words/test.py
"""


def get_max_number_of_words_from_sentences(sentences: list[str]) -> int:
    words_number = []
    for sentence in sentences:
        if sentence != "":
            words_number.append(len(sentence.split(" ")))
        else:
            words_number.append(0)
    return max(words_number)
