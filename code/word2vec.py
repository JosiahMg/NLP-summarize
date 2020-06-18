import logging
import gensim.downloader as api

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


"""
直接加载训练好的word2vec模型  需要翻墙才可下载
下载到的路径：C:\Users\86153\AppData\Local\Temp\
"""

wv = api.load('word2vec-google-news-300')
for i, word in enumerate(wv.vocab):
    if i == 10:
        break
    print(word)


# word2vec无法表示出不在其字典中的词，但是fashtext可以
try:
    vec_cameroon = wv['cameroon']
except KeyError:
    print("The word 'cameroon' does not appear in this model")

# You can see how the similarity intuitively decreases as the words get less and less similar.
pairs = [
    ('car', 'minivan'),   # a minivan is a kind of car
    ('car', 'bicycle'),   # still a wheeled vehicle
    ('car', 'airplane'),  # ok, no wheels, but still a vehicle
    ('car', 'cereal'),    # ... and so on
    ('car', 'communism'),
]
for w1, w2 in pairs:
    print('%r\t%r\t%.2f' % (w1, w2, wv.similarity(w1, w2)))

# print the 5 top of similar words to "car" or "minivan"
print(wv.most_similar(positive=['car', 'minivan'], topn=5))

# which of the below does not belong in the sequence?
print(wv.doesnt_match(['fire', 'water', 'land', 'sea', 'car']))


"""
Storing and loading models
"""
# You can store/load models using the standard gensim methods:


