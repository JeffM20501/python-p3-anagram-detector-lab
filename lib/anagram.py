# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word=word
    
    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, value):
        if isinstance(value, str):
            self._word=value
        else:
            print("Word need to be a string!")
    
    def match(self, arr):
        hold_anagram=[]
        for anagram in arr:
            if sorted(self.word)==sorted(anagram):
                hold_anagram.append(anagram)
        return hold_anagram

word=Anagram("jeff").match(["effj","man", "jffe"])