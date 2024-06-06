from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        n = len(hand)

        if n % groupSize != 0:
            return False

        count = Counter(hand)

        while count:
            curr = min(count)
            
            for i in range(groupSize):
                if count[curr + i] == 0:
                    return False
                
                count[curr + i] -= 1
                if count[curr + i] == 0:
                    del count[curr + i]

        return True
