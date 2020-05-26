import torch
import torchtext
from torchtext import vocab
# 预先训练好的词向量
gv = torchtext.vocab.GloVe(name='6B', dim=50)
# 40万个词，50个维度
len(gv.vectors), gv.vectors.shape
# 获得单词的在Glove词向量中的索引(坐标)
gv.stoi['tokyo']
# 查看tokyo的词向量
gv.vectors[1363]
# 可以把坐标映射回单词
gv.itos[1363]

# 把tokyo转换成词向量
def get_wv(word):
    return gv.vectors[gv.stoi[word]]
get_wv('tokyo')

# 找到距离最近的10个单词
def sim_10(word, n=10):
    all_dists = [(gv.itos[i], torch.dist(word, w)) for i, w in enumerate(gv.vectors)]
    return sorted(all_dists, key=lambda t: t[1])[:n]
sim_10(get_wv('tokyo'))

def analogy(w1, w2, w3, n=5, filter_given=True):
    print(f'[ {w1} : {w2} :: {w3} : ? ]')
    
    # w2 - w1 + w3 = w4
    closest_words = sim_10(get_wv(w2) - get_wv(w1) + get_wv(w3))

    # 过滤防止输入参数出现在结果中
    if filter_given:
        closest_words = [t for t in closest_words if t[0] not in [w1, w2, w3]]
    print(closest_words[:2])

analogy('beijing', 'china', 'tokyo')
# [ beijing : china :: tokyo : ? ]
# [('japan', tensor(2.7869)), ('japanese', tensor(3.6377))]

