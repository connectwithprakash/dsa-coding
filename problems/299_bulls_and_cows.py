class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hash_map = {}
        bull_count = 0
        cows_count = 0

        # Bull count
        for index in range(len(secret)):
            if (secret[index] == guess[index]):
                bull_count += 1
            else:
                if secret[index] in hash_map:
                    hash_map[secret[index]] += 1
                else:
                    hash_map[secret[index]] = 1
        
        # Cow count
        for index in range(len(guess)):
            if (secret[index] != guess[index]) and (hash_map.get(guess[index], 0)):
                hash_map[guess[index]] -= 1
                cows_count += 1
                
        return f"{bull_count}A{cows_count}B"

