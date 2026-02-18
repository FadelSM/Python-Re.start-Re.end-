import re

s = input()
k = input()

# Use re.finditer to find all non-overlapping occurrences
matches = list(re.finditer(f'(?={re.escape(k)})', s))  # use lookahead to allow overlapping

if matches:
    for m in matches:
        start = m.start()
        end = start + len(k) - 1
        print(f'({start}, {end})')
else:
    print("(-1, -1)")
