import jieba
jieba.enable_paddle() # 0.4版本以后支持paddle模式
strings = ['我来自极客大学', 'Python进阶训练营真好玩']

for string in strings:
    result = jieba.cut(string, cut_all=False) # 精确模式
    print('Default Mode: ' + '/'.join(list(result)))

for string in strings:
    result = jieba.cut(string, cut_all=True) # 全模式
    print('Full Mode: ' + '/'.join(list(result)))


for string in strings:
    result = jieba.cut(string, use_paddle=True) # paddle模式
    print('Paddle Mode: ' + '/'.join(list(result)))

result = jieba.cut('钟南山院士接受采访新冠不会二次暴发') # 默认是精确模式
print('/'.join(list(result)))
# "新冠" 没有在词典中，但是被Viterbi算法识别出来了

result = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造') # 搜索引擎模式
print('Search Mode: ' + '/'.join(list(result)))
