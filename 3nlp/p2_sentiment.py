import pandas as pd
from snownlp import SnowNLP

# 加载爬虫的原始评论数据
df = pd.read_csv('book_utf8.csv')
# 调整格式
df.columns = ['star', 'vote', 'shorts']
star_to_number = {
    '力荐' : 5,
    '推荐' : 4,
    '还行' : 3,
    '较差' : 2,
    '很差' : 1
}
df['new_star'] = df['star'].map(star_to_number)
# 用第一个评论做测试
first_line = df[df['new_star'] == 3].iloc[0]
text = first_line['shorts']
s = SnowNLP(text)
print(f'情感倾向: {s.sentiments} , 文本内容: {text}')

# 封装一个情感分析的函数
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

df["sentiment"] = df.shorts.apply(_sentiment)
# 查看结果
df.head()
# 分析平均值
df.sentiment.mean() 


# 训练模型
# from snownlp import sentiment
# sentiment.train('neg.txt','pos.txt')
# sentiment.save('sentiment.marshal')

del df['star']
del df['vote']
order = ['new_star', 'shorts', 'sentiment']
df = df[order]
df.rename(columns={'new_star':'n_star','shorts':'short'},inplace=True) 
df.to_csv('result.csv', index=None)