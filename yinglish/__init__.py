import random

import jieba
import jieba.posseg as pseg
jieba.setLogLevel(20)

import spacy
_nlp = spacy.load("en_core_web_sm")


def _词转换(x, y, 淫乱度):
    if random.random() > 淫乱度:
        return x
    if x in {'，', '。'}:
        return '……'
    if len(x) > 1 and random.random() < 0.5:
        return f'{x[0]}……{x}'
    else:
        if y == 'n' and random.random() < 0.5:
            x = '〇' * len(x)
        return f'……{x}'


def _word_convert(x, y, yinluanity):
    if random.random() > yinluanity:
        return x
    if x in {', ', '. '}:
        return '...'
    if len(x) > 1 and random.random() < 0.5:
        return f'{x[0]}...{x}'
    else:
        if y == 'NOUN' and random.random() < 0.5:
            x = '〇' * int(len(x)/2+0.5)
        return f'...{x}'


def _en_pseg(s):
    doc = _nlp(s)
    return [(str(token), token.pos_) for token in doc]


def chs2yin(s, 淫乱度=0.5):
    return ''.join([_词转换(x, y, 淫乱度) for x, y in pseg.cut(s)])


def eng2yin(s, yinluanity=0.5):
    result = ' '.join([_word_convert(x, y, yinluanity) for x, y in _en_pseg(s)])
    result = result.replace(' .', '.').replace('....', '...')
    return result

if __name__ == '__main__':
    print(chs2yin('不行，那里不行。'))
