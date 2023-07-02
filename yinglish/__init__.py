import random

import jieba
import jieba.posseg as pseg
jieba.setLogLevel(20)


def _词转换(x, y, 淫乱度):
    if random.random() > 淫乱度:
        return x
    if x in {'，', '。'}:
        return '……'
    if x in {'!', '！'}:
        return '❤'
    if len(x) > 1 and random.random() < 0.5:
        return f'{x[0]}……{x}'
    else:
        if y == 'n' and random.random() < 0.5:
            x = '〇' * len(x)
        return f'……{x}'


def chs2yin(s, 淫乱度=0.5):
    return ''.join([_词转换(x, y, 淫乱度) for x, y in pseg.cut(s)])

a = ["!", "…", "♡", "♥"]

# 一个字符串转繁体或者火星文
def _to_huoxin(s:str):
    dict_1_2 = {}
    dict_1_3 = {}
    dict_2_3 = {}
    # 打开文件
    with open('huoxin.dat', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line = line.split(' ')
            dict_1_2[line[0]] = line[1]
            dict_1_3[line[0]] = line[2]
            dict_2_3[line[0]] = line[2]
    s_out = ""
    for i in s:
        x = random.random()
        if x < 0.3:
            if i in dict_1_3:
                s_out += dict_1_3[i]
            elif i in dict_2_3:
                s_out += dict_2_3[i]
            else:
                s_out += i
        elif x < 0.9:
            if i in dict_1_2:
                s_out += dict_1_2[i]
            elif i in dict_2_3:
                s_out += dict_2_3[i]
            else:
                s_out += i
        else:
            s_out += i
    return s_out


# 一个词语转成淫语
def _convert(s:str, degree: float):
    x = random.random()
    if x > degree:
        return s
    s = _to_huoxin(s)

    # 前缀
    prefix = ""
    N = random.randint(0, 3)
    for i in range(N):
        M = random.randint(1, 3)
        prefix = prefix + random.choice(a)*M
    # 后缀
    suffix = ""
    N = random.randint(0, 3)
    for i in range(N):
        M = random.randint(1, 3)
        suffix = suffix + random.choice(a)*M
    isPrefix = False
    isSuffix = False
    if random.random() < 0.5:
        s = prefix + s
    if random.random() < 0.5:
        s = s + suffix
    return s

# 一句话转成淫语（先分词，然后一个个转）
def convert_to_yinglish(s:str, degree = 1)->str:
    s_splited = jieba.cut(s)
    s_yinglish = ''
    for word in s_splited:
        s_yinglish += _convert(word, degree)
    return s_yinglish

if __name__ == '__main__':
    s = '不行，那里不行。'
    s1 = chs2yin(s)
    s2 = convert_to_yinglish(s)
    print(s)
    print(s1)
    print(s2)
