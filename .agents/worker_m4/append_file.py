import sys
target, text = sys.argv[1], sys.argv[2]
with open(target, 'a', encoding='utf-8') as out:
    out.write(text)
