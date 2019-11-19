# 07-dec-2018


### 1 - writing your own grammar engine?

- just an attempt to start understanding strings with rules
- The idea is that assuming your input is character based tokens; what it takes to write a engine that can evaluate the string based on give rules. Don't know what the algorithm is called; and am trying to do it from experimentation to learn.
- TODO: add function calls and actual evalutation

```python
class Grammar:

	"""The idea is to have some rules and try to make a reduction with them of the given string"""

	def __init__(self, rules):
		"""rules is a list of compression rules"""
		self.rules = rules

	def items(self):
		"""get a array of grammar rules"""
		return [  (x.split(":")[0].strip(), x.split(":")[1].strip())  for x in self.rules.split(";") if len(x.strip()) >0 ] 

	def match_prefix(self,sentence):
		"""visit grammar rules and take the first one which matches and return that"""
		if len(sentence) == 0 or sentence is None:
			return None,None

		for k,v in self.items():
			if sentence.startswith(v):
				return k, sentence[len(v):]
		return None,None


	def recursive_compression(self,sentence,depth=0):
		"""process the sentence to shorten it using the grammar rules"""

		if len(sentence) == 0:
			return ""
		
		print( " "*depth +  sentence)
		matched_token , updated_sentence = self.match_prefix(sentence)

		if matched_token != None:
			return self.recursive_compression(matched_token + updated_sentence,depth + 1)
		else:
			return sentence[0] + self.recursive_compression(sentence[1:],depth + 1)

		
if __name__ == '__main__':

	rules= """
	E : *EE;
        E : +EE;
	E : 0;
	E : 1;
	"""


	

	g=Grammar(rules)
	
	while True:
		_ = raw_input('enter string >> ')
		print 'round : ' + '0'		
		c = g.recursive_compression(_)
		i = 0
		while c != _:
			_  = c
			c = g.recursive_compression(_)
			i = i + 1
			print 'round : ' + str(i)

		print c 
```
