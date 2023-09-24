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
    max_sentence_length = 0
    for sentence in sentences:
        sentence_length = len(sentence.split(" "))
        if sentence and sentence_length > max_sentence_length:
            max_sentence_length = sentence_length
    return max_sentence_length
