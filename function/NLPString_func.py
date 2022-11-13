from eunjeon import Mecab
import nltk
import json
from function.DataManage import search_word

# import mecab
mecab = Mecab()


# POS tag a sentence
# sentence = input("문장 입력하시오:")
def getNLP(sentence):
    if sentence == '':
        json_object = \
            {
                "for_back": {
                    "nnp": [],
                    "word": [],
                    "cant": []
                },
                "for_front": {
                    "nnp": [],
                    "noun": [],
                    "verb": []
                }
            }
        return json_object
    words = Mecab().pos(sentence)

    verb_re, noun_re, js_word, word_re, cant_word = [], [], [], [], []
    nnp = []

    grammar = """
    NP: {<N.*>*<Suffix>?}   # Noun phrase
    AP: {<VA.*>*}            # Adjective phrase
    VX: {<VX.*>*}
    VV: {<VV.*>*}         # Verb phrase
    MP: {<M.*>*}
    VC: {<VC*.*>*}
    EC: {<EC.*>*}
    """

    parser = nltk.RegexpParser(grammar)
    for subtree in parser.parse(words).subtrees():
        if subtree.label() == 'NP':
            if list(subtree)[0][1] == 'NNP':
                nnp.append(list(subtree)[0][0])
                word_re.append(list(subtree)[0][0])
            else:
                noun_re.append(list(subtree)[0][0])
                word_re.append(list(subtree)[0][0])
        if list(subtree)[0][0][-1] == "다" or list(subtree)[0][0][-1] == "요":
            if subtree.label() == 'VV':
                verb_re.append(list(subtree)[0][0])
                word_re.append(list(subtree)[0][0])
            if subtree.label() == 'AP':
                verb_re.append(list(subtree)[0][0])
                word_re.append(list(subtree)[0][0])
            if subtree.label() == 'VX':
                verb_re.append(list(subtree)[0][0])
                word_re.append(list(subtree)[0][0])
        else:
            if subtree.label() == 'VV':
                verb_re.append(list(subtree)[0][0] + "다")
                word_re.append(list(subtree)[0][0] + "다")
            if subtree.label() == 'AP':
                verb_re.append(list(subtree)[0][0] + "다")
                word_re.append(list(subtree)[0][0] + "다")
            if subtree.label() == 'VX':
                verb_re.append(list(subtree)[0][0] + "다")
                word_re.append(list(subtree)[0][0] + "다")
        if subtree.label() == 'MP':
            noun_re.append(list(subtree)[0][0])
            word_re.append(list(subtree)[0][0])

    for i in word_re:
        try:
            js_word.append([search_word(i)[0], search_word(i)[1]])
        except:
            cant_word.append(i)

    json_object = \
        {
            "for_back": {
                "nnp": nnp,
                "word": js_word,
                "cant": cant_word
            },
            "for_front": {
                "nnp": nnp,
                "noun": noun_re,
                "verb": verb_re
            }
        }
    return json_object
# print(NLP(sentence))
