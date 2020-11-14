# 淫语翻译机！

能把中文翻译成淫语的翻译机！


## 样例

```python
import yinglish

s = '不行，那里不行。'
print(yinglish.chs2yin(s))
# 不行，那……那里不行……
```


## 接口说明

```python
def chs2yin(s, 淫乱度=0.5):
```

s是原字符串，淫乱度是0~1的实数，越大越淫乱，表示每个词语被转化的概率。


## 安装

```bash 
pip install git+https://github.com/RimoChan/yinglish.git
```

然后import就行了。


## 结束

就这样，大家88<sub>(溜了溜了)</sub>。
