import sys

input = lambda: sys.stdin.readline()

n = int(input())
words = [input().strip() for _ in range(n)]
sorted_words = sorted(words)
prefixes = set()
max_count = 0

for i in range(1, n):
    prefix = ''
    previous_word = sorted_words[i - 1]
    current_word = sorted_words[i]
    
    if previous_word == current_word:
        continue
    
    for j in range(min(len(previous_word), len(current_word))):
        if previous_word[j] != current_word[j]:
            break
        
        prefix += current_word[j]
    
    if len(prefix) > max_count:
        prefixes = {prefix}
        max_count = len(prefix)
    elif len(prefix) == max_count:
        prefixes.add(prefix)

s = None
t = None
p = ''
for word in words:
    if s is None:
        for prefix in prefixes:
            if not word.startswith(prefix):
                continue
            
            s = word
            p = prefix
            break
    
    elif t is None and s != word and word.startswith(p):
        t = word
        
print(s, t, sep='\n') 
