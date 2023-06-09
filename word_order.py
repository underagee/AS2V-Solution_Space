# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
word_count = {}

for _ in range(n):
    word = input().strip()
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

distinct_words = len(word_count)
occurrences = [word_count[word] for word in word_count]

print(distinct_words)
print(*occurrences)
