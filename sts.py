# -*- coding:utf-8 -*-
from gensim import corpora, models, similarities
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords

def load_sentences(file_name):
    with open(file_name, "r") as f:

        def spilt_to_sentences(line):
            line = line.lower()
            line = line[:-1] # remove \n
            lines = line.split("\t") #spilt with \t
            #split two sentence
            lines = map(wt, lines)
            return lines

        sentences = [spilt_to_sentences(line) for line in f.readlines()]
        return sentences

def build_dics(sentences):
    texts = [text for sentence in sentences for text in sentence]
    def remove(texts, stops):
        texts = [[w for w in text if w not in stops] for text in texts]
        return texts
    e_p = [".", ",", "!", "?"]
    stops = stopwords.words("english")
    stops += e_p
    texts =remove(texts, stops)
    return corpora.Dictionary(texts)

def word_to_dic(sentences, dics):
    def f(sentence, dics=dics):
        return map(dics.doc2bow, sentence)
    return map(f, sentences)

def count_similarty(vector):
    index = similarities.MatrixSimilarity(vector)
    sim = index[vector[1]][0]
    return sim

if __name__ == "__main__":
    sentences = load_sentences("STS.txt")
    dics = build_dics(sentences)
    vectors = word_to_dic(sentences, dics)
    sims = map(count_similarty, vectors)
    with open("similarities.txt", "w") as f:
        for sim in sims:
            f.write(str(sim)+"\n")
