class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Counter({'i': 3, 'n': 3, 'd': 2, 'r': 2, 'h': 2, 'e': 2, 'y': 2, 't': 1, 'o': 1, 'p': 1, 'l': 1, 'a': 1, 'z': 1})
        
        Counter({'t': 4, 'i': 4, 'n': 4, 'r': 3, 'e': 3, 'h': 2, 'y': 2, 'l': 2, 'm': 2, 'o': 1, 'p': 1, 'a': 1})
        """
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        s2_counter = defaultdict(int)
        have = 0
        need = len(s1_counter)
        for i in range(len(s1)):
            s2_counter[s2[i]] += 1
            char = s2[i]
            if char in s1_counter and s2_counter[char] == s1_counter[char]:
                have += 1
        # print(s1_counter)
        if have == need:
            return True
        l = 0
        
        
        for r in range(len(s1), len(s2)):
            char = s2[r]
            s2_counter[char] += 1
            if char in s1_counter and s2_counter[char] == s1_counter[char]:
                have += 1
            char = s2[l]
            s2_counter[char] -= 1
            if char in s1_counter and s2_counter[char] < s1_counter[char]:
                have -= 1
            if s2_counter[char] == 0:
                del s2_counter[char]
            if have == need:
                return True
            if s1_counter == s2_counter:
                return True
            l += 1
            # print(s2_counter)
        # print(have, need)
        return False