from janome.tokenizer import Tokenizer

def count_and_vectorize(d1, d2, sentence):
    PN_table = [0, 0, 0, 0] #陰性、中性、陽性, 極性持ち語数
    t = Tokenizer()
    words = []
    for token in t.tokenize(sentence):
        words.append(token.base_form)

    for i in range(len(words)):
        if words[i] in d1:
            if d1[words[i]] == -1:
                PN_table[0] += 1
            elif d1[words[i]] == 0:
                PN_table[1] += 1
            elif d1[words[i]] == 1:
                PN_table[2] += 1
            PN_table[3] += 1
        elif words[i] in d2:
            if d1[words[i]] == -1:
                PN_table[0] += 1
            elif d1[words[i]] == 1:
                PN_table[2] += 1
            PN_table[3] += 1
    return PN_table