#Bull and Cows: https://leetcode.com/problems/bulls-and-cows
from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sC = Counter(secret)
        extra = ""
        bullCount = 0
        cowCount = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bullCount += 1
                sC[secret[i]] -= 1
            else:
                extra += guess[i]
        for i in range(len(extra)):
            if sC[extra[i]] > 0:
                cowCount += 1
                sC[extra[i]] -= 1
        return f'{bullCount}A{cowCount}B'

#here What I did Was, I used a COunters for  secret
# in the first loop, i counted the bulls, and decreased the count of that cow in sC and i added all the numbers which are not bull in guess to extra
# So that it will be easy to find the number of cows.
# now in the second for loop, i iterated over the extra, and checked if that digit is there in secret and decremented the count.