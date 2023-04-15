# load vocabs
with open("src_vocab.txt", "r", encoding="utf-8") as f:
    source_vocab = f.read().splitlines()
with open("tgt_vocab.txt", "r", encoding="utf-8") as f:
    target_vocab = f.read().splitlines()

# load translation model from file
translation_prob = {}
with open("translation_prob.txt", "r", encoding="utf-8") as f:
    for line in f:
        source_word, target_word, count = line.split()
        if int(source_word) not in translation_prob:
            translation_prob[int(source_word)] = {}
        translation_prob[int(source_word)][int(target_word)] = int(count)


print("frequency dictionary")
freq_dictionary = {}
for word in translation_prob:
    max_value = max(translation_prob[word].values())
    freq_dictionary[word] = max_value

# Step 3: Find the most probable translation for each word
print("finding most probable translation for each word...")
# sort translation_prob by source word frequency
sorted_translation_prob = sorted(translation_prob.items(), key=lambda x: freq_dictionary[x[0]], reverse=True)
print("translation model sorted")
taken = set()
dictionary = {}
for i in range(0, len(sorted_translation_prob)):
    src_emb = sorted_translation_prob[i][0]
    # sort sorted_translation_prob[i][1].items() by highest
    max_keys = sorted(sorted_translation_prob[i][1].items(), key=lambda x: x[1], reverse=True)

    # choose the hightest probability word that has not been taken
    for j in range(0, len(max_keys)):
        target = max_keys[j][0]
        if target not in taken:
            break
    taken.add(target)
    dictionary[src_emb] = target

# print vocab for dictionary
for key in dictionary:
    print(source_vocab[key], target_vocab[dictionary[key]])

# save dictionary
with open("dictionary.txt", "w", encoding="utf-8") as f:
    for key in dictionary:
        f.write(source_vocab[key] + " " + target_vocab[dictionary[key]] + "\n")

