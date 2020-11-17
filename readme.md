# 淫语翻译机！

能把中文和英文翻译成淫语的翻译机！

<sub>(其实灵感是来自北京地铁站，那个写站名的告示牌真的好色啊2333)</sub>


## 样例

```python
import yinglish

s = '不行，那里不行。'
print(yinglish.chs2yin(s))
# 不行，那……那里不行……

s2 = '吃葡萄不吐葡萄皮。'
print(yinglish.chs2yin(s2))
# ……吃〇〇不吐葡……葡萄皮……

s3 = 'Although games are great, but I like your cooking better.'
print(yinglish.eng2yin(s3))
# A...Although g...games...are great..., b...but...I like your...〇〇〇〇 b...better...
```


## 接口说明

```python
def chs2yin(s, 淫乱度=0.5):
```

s是原字符串，淫乱度是0~1的实数，越大越淫乱，表示每个词语被转化的概率。

```python
def eng2yin(s, yinluanity=0.5):
```

s是原字符串，yinluanity是0~1的实数，越大越淫乱，表示每个词语被转化的概率。


## 安装

首先，你需要安装一个Python(3.6以上版本)。

然后——
```bash 
pip install git+https://github.com/RimoChan/yinglish.git
```

最后`import yinglish`就行了。


## 结束

就这样，大家88<sub>(溜了溜了)</sub>。
