class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word = sentence.split(" ")
        # dictionary.sort()
        for i in range(len(dictionary)):
            
            for j in range(len(word)):
                k = 0
                hai = True
                while k < len(dictionary[i]) and k < len(word[j]):
                    if dictionary[i][k] != word[j][k]:
                        hai = False
                        break
                    k += 1
                if hai:
                    if len(word[j]) > len(dictionary[i]):
                        word[j] = dictionary[i]
    
        return " ".join(word)