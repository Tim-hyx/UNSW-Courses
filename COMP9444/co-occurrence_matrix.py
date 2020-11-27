import re

sentence, size, r = input('input sentence: '), int(
    input('input window size: ')) // 2, '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~。！，]+'
sentence = re.sub(r, ' ', sentence)
sentence = [word.lower() for word in sentence.split()]
words = sorted(set(sentence))
pad = max([len(word) for word in words])
matrix = [[' ' * pad] + words]
for i in range(len(words)):
    row = [words[i]] + [0] * len(words)
    for j in range(len(sentence)):
        if words[i] == sentence[j]:
            for k in range(len(words)):
                if words[i] != words[k]: row[k + 1] += sentence[
                                                       max(0, j - size):min(len(sentence), j + size + 1)].count(
                    words[k])
    matrix.append(row)
for row in matrix:
    print(' '.join(str(x).center(pad) for x in row))
