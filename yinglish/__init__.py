import random

import jieba
import jieba.posseg as np # 惊！？
jieba.setLogLevel(20)


def _词转换(x, y, 淫乱度):
    if random.random() > 淫乱度:
        return x
    if x in {'，', '。'}:
        return '……'
    if len(x) > 1 and random.random() < 0.5:
        return f'{x[0]}……{x}'
    else:
        if y == 'n' and random.random() < 0.5:
            x = ''.join(['〇' for _ in x])
        return f'……{x}'


def chs2yin(s, 淫乱度=0.5):
    return ''.join([_词转换(x, y, 淫乱度) for x, y in np.cut(s)])


if __name__ == '__main__':
    print(chs2yin('不行，那里不行。'))
