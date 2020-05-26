import jieba
import jieba.analyse
text = '机器学习，需要一定的数学基础，需要掌握的数学基础知识特别多，如果从头到尾开始学，估计大部分人来不及，我建议先学习最基础的数学知识'
stop_words=r'day0402/extra_dict/stop_words.txt'
# stop_words 的文件格式是文本文件，每行一个词语
jieba.analyse.set_stop_words(stop_words)

textrank = jieba.analyse.textrank(text,
topK=5,                   
withWeight=False)         

import pprint             # pprint 模块提供了打印出任何Python数据结构的类和方法
pprint.pprint(textrank)
