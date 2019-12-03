# 03-dec-2019

### 2 - regular expression parser

- got this question on pramp interview

TODO DP solution from Pramp

```python3
def is_match(text,pattern):

  if not pattern:
    return not text
  first_character= bool(text) and pattern[0] in {'.',text[0]}
  if len(pattern)>=2 and pattern[1]=='*':
    return (is_match(text,pattern[2:])) or ( first_character and is_match(text[1:],pattern))
  else:
    return (first_character and is_match(text[1:],pattern[1:]))
```

### 1 - inverted index vs forward index

https://www.geeksforgeeks.org/difference-inverted-index-forward-index/

