def word_counter(str):
    counts = dict()
    words = str.split()
    print(words)
    for i in words:

        if i in counts:
            counts[i] += 1
           # print(counts)
        else:
            counts[i] = 1

    return counts
print( word_counter(input('enter the phrase')))