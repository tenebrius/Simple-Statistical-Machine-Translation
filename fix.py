import re

with open("ELRC-3569-EUR_LEX_covid.en-fr.en", "r", encoding="utf-8") as f:
    source_sentences = f.readlines()
with open("ELRC-3569-EUR_LEX_covid.en-fr.fr", "r", encoding="utf-8") as f:
    target_sentences = f.readlines()

def fix(sentence):
    # replace punctuation with space using regex
    sentence = re.sub(r'[^\w\s]', ' ', sentence)
    # replace multiple spaces with single space
    sentence = re.sub(r'\s+', ' ', sentence)

    #lowercase
    sentence = sentence.lower()

    return sentence

def create_vocab(sentences):
    vocab = {}
    for sentence in sentences:
        for word in sentence.split():
            if word not in vocab:
                vocab[word] = 1
            else:
                vocab[word] += 1
    #sort vocab by frequency
    vocab = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
    #get only words
    vocab = [x[0] for x in vocab]
    return vocab


print("Fixing sentences")
source_sentences = [fix(sentence) for sentence in source_sentences]
target_sentences = [fix(sentence) for sentence in target_sentences]

# create vocab
print("Creating vocab")
src_vocab = create_vocab(source_sentences)
tgt_vocab = create_vocab(target_sentences)

# split words
# convert sentences to list of words
print("Splitting words")
source_sentences = [x.split() for x in source_sentences]
target_sentences = [x.split() for x in target_sentences]

#convert to embedding
print("Converting to embedding source")

source_sentences = [[src_vocab.index(word) for word in sentence] for sentence in source_sentences]
print("Converting to embedding target")
target_sentences = [[tgt_vocab.index(word) for word in sentence] for sentence in target_sentences]


#write to file
print("Writing to file")
with open("ELRC-3569-EUR_LEX_covid.en-fr.en.tok", "w", encoding="utf-8") as f:
    for sentence in source_sentences:
        f.write(" ".join([str(x) for x in sentence]) + "\n")

with open("ELRC-3569-EUR_LEX_covid.en-fr.fr.tok", "w", encoding="utf-8") as f:
    for sentence in target_sentences:
        f.write(" ".join([str(x) for x in sentence])  + "\n")

#write vocab to file seperated by new line
with open("src_vocab.txt", "w", encoding="utf-8") as f:
    for word in src_vocab:
        f.write(word + "\n")

with open("tgt_vocab.txt", "w", encoding="utf-8") as f:
    for word in tgt_vocab:
        f.write(word + "\n")
