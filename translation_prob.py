# Collect and preprocess the parallel corpus
# target_sentences = ['the cat is sleeping', 'the dog is barking', 'the house is big', 'the car is red', 'the book is interesting', 'the table is wooden', 'the chair is comfortable', 'the tree is tall', 'the flower is beautiful', 'the sun is shining', 'the black cat is hiding', 'the white dog is playful', 'the small house is cozy', 'the blue car is fast', 'the thick book is heavy', 'the round table is modern', 'the leather chair is expensive', 'the green tree is leafy', 'the pink flower is fragrant', 'the bright sun is hot', 'a black cat is crossing the road', 'a brown dog is chasing a ball', 'a small house is for sale', 'a white car is parked on the street', 'a thick book is on the shelf', 'a square table is in the dining room', 'an old chair is in the attic', 'a tall tree is in the park', 'a purple flower is in the garden', 'the sun is setting', 'the cat is meowing', 'the dog is wagging its tail', 'the house is on fire', 'the car is broken down'
#                               , 'the sky is blue', 'the grass is green', 'the ocean is vast', 'the mountain is tall', 'the bird is singing', 'the fish is swimming', 'the butterfly is colorful', 'the bee is buzzing', 'the river is flowing', 'the moon is full', 'the sun is setting in the west', 'the stars are twinkling', 'the rainbow is beautiful', 'the snow is falling', 'the wind is blowing', 'the cloud is fluffy', 'the thunder is loud', 'the lightning is bright', 'the tornado is dangerous', 'the hurricane is coming', 'the volcano is erupting', 'the earthquake is shaking', 'the tsunami is approaching', 'the flood is rising', 'the drought is worsening', 'the famine is devastating', 'the war is raging', 'the peace is fragile', 'the love is strong', 'the hate is destructive', 'the happiness is contagious', 'the sadness is overwhelming', 'the anger is boiling', 'the fear is paralyzing', 'the courage is inspiring', 'the hope is reassuring', 'the faith is unshakable', 'the trust is invaluable', 'the friendship is precious', 'the family is important', 'the work is rewarding', 'the study is challenging', 'the travel is exciting', 'the food is delicious', 'the drink is refreshing', 'the music is soothing', 'the art is inspiring']
#
# source_sentences = ['le chat dort', 'le chien aboie', 'la maison est grande', 'la voiture est rouge', 'le livre est intéressant', 'la table est en bois', 'la chaise est confortable', "arbre est grand", 'la fleur est belle', 'le soleil brille', 'le chat noir se cache', 'le chien blanc est joueur', 'la petite maison est confortable', 'la voiture bleue est rapide', 'le livre épais est lourd', 'la table ronde est moderne', 'la chaise en cuir est chère', "arbre vert est feuillu", 'la fleur rose est parfumée', 'le soleil brillant est chaud', 'un chat noir traverse la route', 'un chien brun chasse une balle', 'une petite maison est à vendre', 'une voiture blanche est garée dans la rue', 'un livre épais est sur l étagère', 'une table carrée est dans la salle à manger', 'une vieille chaise est dans le grenier', 'un grand arbre est dans le parc', 'une fleur violette est dans le jardin', 'le soleil se couche', 'le chat miaule', 'le chien remue la queue', 'la maison est en feu', 'la voiture est en panne'
#                     , 'le ciel est bleu', 'l herbe est verte', 'l océan est vaste', 'la montagne est haute', 'l oiseau chante', 'le poisson nage', 'le papillon est coloré', 'l abeille bourdonne', 'la rivière coule', 'la lune est pleine', 'le soleil se couche à l ouest', 'les étoiles scintillent', 'l arc-en-ciel est beau', 'la neige tombe', 'le vent souffle', 'le nuage est moelleux', 'le tonnerre est fort', 'l éclair est brillant', 'la tornade est dangereuse', 'l ouragan arrive', 'le volcan est en éruption', 'le tremblement de terre secoue', 'le tsunami approche', 'la crue est en hausse', 'la sécheresse s aggrave', 'la famine est dévastatrice', 'la guerre fait rage', 'la paix est fragile', 'l amour est fort', 'la haine est destructrice', 'le bonheur est contagieux', 'la tristesse est accablante', 'la colère bouillonne', 'la peur est paralysante', 'le courage est inspirant', 'l espoir est rassurant', 'la foi est inébranlable', 'la confiance est inestimable', 'l amitié est précieuse', 'la famille est importante', 'le travail est gratifiant', 'l étude est stimulante', 'le voyage est excitant', 'la nourriture est délicieuse', 'la boisson est rafraîchissante', 'la musique est apaisante', 'l art est inspirant']

# Step 1: Load data and create vocabulary
#   source_sentences = f.readlines()
# UnicodeDecodeError: 'gbk' codec can't decode byte 0x93 in position 1814: illegal multibyte sequence

with open("ELRC-3569-EUR_LEX_covid.en-fr.en.tok", "r", encoding="utf-8") as f:
    source_sentences = f.read().splitlines()
with open("ELRC-3569-EUR_LEX_covid.en-fr.fr.tok", "r", encoding="utf-8") as f:
    target_sentences = f.read().splitlines()



# convert sentences to list of words
print("splitting sentences into words...")
source_sentences = [[int(i) for i in x.split()] for x in source_sentences]
target_sentences = [[int(i) for i in x.split()] for x in target_sentences]

# Step 2: Build the translation model
print("building translation model...")
translation_prob = {}
for i in range(len(source_sentences)):
    source_words = source_sentences[i]
    target_words = target_sentences[i]
    for j in range(len(source_words)):
        source_word = source_words[j]
        for k in range(len(target_words)):
            target_word = target_words[k]
            if source_word not in translation_prob:
                translation_prob[source_word] = {}
            if target_word not in translation_prob[source_word]:
                translation_prob[source_word][target_word] = 0
            translation_prob[source_word][target_word] += 1

print("translation model built")

# load vocabs
with open("src_vocab.txt", "r", encoding="utf-8") as f:
    source_vocab = f.read().splitlines()
with open("tgt_vocab.txt", "r", encoding="utf-8") as f:
    target_vocab = f.read().splitlines()


freq_dictionary = {}
for word in translation_prob:
    max_value = max(translation_prob[word].values())
    max_keys = [k for k, v in translation_prob[word].items() if v == max_value]
    freq_dictionary[word] = max_value

# Step 3: Find the most probable translation for each word
print("finding most probable translation for each word...")
most_probable_translation = {}
for source_word in translation_prob:
    max_prob = 0
    max_target_word = ""
    for target_word in translation_prob[source_word]:
        prob = translation_prob[source_word][target_word] / freq_dictionary[source_word]
        if prob > max_prob:
            max_prob = prob
            max_target_word = target_word
    most_probable_translation[source_word] = max_target_word



# save translation model
with open("translation_prob.txt", "w", encoding="utf-8") as f:
    for source_word in translation_prob:
        for target_word in translation_prob[source_word]:
            f.write(str(source_word) + " " + str(target_word) + " " + str(translation_prob[source_word][target_word]) + "\n")
