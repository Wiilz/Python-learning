import random

noun_file = open("nouns.txt",'r')
nouns = noun_file.readlines()
noun_file.close()

adjective_file = open("adjectives.txt",'r')
adjectives = adjective_file.readlines()
adjective_file.close()

verb_file = open("verbs.txt",'r')
verbs = verb_file.readlines()
verb_file.close()

adverb_file = open("adverbs.txt",'r')
adverbs = adverb_file.readlines()
adverb_file.close()

noun = random.choice(nouns)
no = noun.strip()
adjective = random.choice(adjectives)
adj = adjective.strip()
verb = random.choice(verbs)
ver = verb.strip()
adverb = random.choice(adverbs)
adv = adverb.strip()

print "The",adj,no,ver,adv
