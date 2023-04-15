# load dictionary
dictionary = {}
with open("dictionary.txt", "r", encoding="utf-8") as f:
    for line in f:
        src, tgt = line.split()
        dictionary[src] = tgt

def translate(sentence):
    source_words = sentence.split()
    target_words = []
    for source_word in source_words:
        if source_word in dictionary:
            target_word = dictionary[source_word]
        else:
            target_word = source_word
        target_words.append(target_word)
    return " ".join(target_words)


# Test the translation algorithm
source_sentence = '''
other supporting and complementary actions necessary in the framework of the Union Civil Protection Mechanism to achieve a high level of protection against disasters and enhance the Union's state of preparedness to respond to disasters,
By way of information, these amounts derive from contributions from the EFTA States entered against Article 6 3 0 of the statement of revenue, which constitute assigned revenue in accordance with points (b), (e) and (f) of Article 21(2) of the Financial Regulation; they give rise to the provision of corresponding appropriations and to implementation under the ‘European Economic Area' Annex to this part of the statement of expenditure in this section, which forms an integral part of the general budget.
studies, meeting of experts, information and publications directly linked to the achievement of the objective of the emergency support, '''
translated_sentence = translate(source_sentence.lower())
print(translated_sentence)  # Output: ['le', 'chat', 's\'est', 'assis', 'sur', 'le', 'tapis']
