# Diga ao python que usaremos funcionalidades aleatórias importando o módulo random
import random


# Faça três listas: uma de verbos (verbs), uma de Adjetivos (adjectives) e uma de substantivos Noun
verbs = ['Leverage', 'Sync', 'Target', 'Gamify', 'Offline', 'Crowd-sourced', '24/7', 'Lean-in', '30,000 foot']

adjectives = ['A/B Tested', 'Freemium', 'Hyperlocal', 'Siloed', 'B-to-B', 'Oriented', 'Cloud-based', 'API-based']

nouns = ['Marley Adopter', 'Low-hanging Fruit', 'Pipeline', 'Splash Page', 'Productivity', 'Process', 'Tipping Point',
         'Paradigm']

# Escolha um verbo, um adjetivo e um substantivo de cada lista
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# Agora crie a frase "somando" as palavras
phrase = verb + ' ' + adjective + ' ' + noun

# Faça output da frase
print(phrase)
