class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0: return False
        deck = Counter(hand)
        hand.sort()
        for n in hand:
            if deck[n]:
                for i in range(n, n + groupSize):
                    if deck[i]:
                        deck[i] -= 1
                    else:
                        return False
        return True