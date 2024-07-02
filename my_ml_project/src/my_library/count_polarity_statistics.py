def count(d1, d2, sentence):
    PN_table = [0, 0, 0] #陰性、中性、陽性
    string=""
    for i in range(len(sentence)):
    #for word in sentence:
        word=sentence[i]
        string+=word
        if word == "けど":#逆接の助詞
            PN_table=[0.1*pn for pn in PN_table]
            #ここの係数については、再考
        a=1
        if i+1<len(sentence) and sentence[i+1]=="ない":
            a=-1 #「ない」の直前では、極性を反転させる
        if word in d1:
            kyokusei=a*d1[word]+1
            PN_table[kyokusei]+=1
            string+=str(kyokusei)
        elif word in d2:
            kyokusei=a*d2[word]+1
            PN_table[kyokusei]+=1
            string+=str(kyokusei)
    return PN_table