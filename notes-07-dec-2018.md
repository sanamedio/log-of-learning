# 07-dec-2018


### 1 - writing your own grammar engine?

- just an attempt to start understanding strings with rules

```
class Grammar:
        rules= """
        N : N*0;
        N : N+1;
        N : N0;
        N : N1;
        N : 1;
        N : 0;  
        """
        def __init__(self):
                print(self.rules)

        def items(self):
                return [  (x.split(":")[0].strip(), x.split(":")[1].strip())  for x in self.rules.split(";") if len(x.strip()) >0 ]


GRAMMAR=Grammar()




def match_prefix(sentence):

        if len(sentence) == 0 or sentence is None:
                return None,None

        for k,v in GRAMMAR.items():
                if sentence.startswith(v):
                        return k, sentence[len(v):]
        return None,None


def recursive_compression(sentence):

        print(sentence)

        if len(sentence) == 0:
                return ""

        matched_token , updated_sentence = match_prefix(sentence)

        if matched_token != None:
                return recursive_compression(matched_token + updated_sentence)
        else:
                return sentence[0] + recursive_compression(sentence[1:])


if __name__ == '__main__':

        while True:
                _ = raw_input()
                print(recursive_compression(_))

```
