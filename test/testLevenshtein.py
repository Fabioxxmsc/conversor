import Levenshtein

# Exemplo de cálculo da distância de edição entre duas palavras
word1 = "hello"
word2 = "hal1o"
distance = Levenshtein.distance(word1, word2)
print("Distância de edição entre '{}' e '{}' é: {}".format(word1, word2, distance))