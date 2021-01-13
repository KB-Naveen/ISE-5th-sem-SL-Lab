from functools import reduce
from collections import Counter

word_freq = Counter(open('sample.txt').read().split())
print("Word frequency :",word_freq)

sorted_freq = sorted(dict(word_freq).items(),key=lambda d:d[1],reverse=True)
print("Top 10 most occurence :")
for i in range(10):
    print(sorted_freq[i])

word_len = []
for i in sorted_freq:
    word_len.append(i[1])
print("List of word lengths :",word_len)

avg = (reduce(lambda a,b:a+b,word_len))/len(word_len)
print("Average Length :",avg)

odd_sq = [x**2 for x in word_len if x%2==1]
print("Odd squares :",odd_sq)