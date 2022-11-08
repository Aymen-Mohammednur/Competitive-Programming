class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        counter_s = defaultdict(int)
        have = 0
        need = len(counter_t)
        ans = [float('inf'), None, None]
        l = 0
        for r in range(len(s)):
            counter_s[s[r]] += 1
            if s[r] in counter_t and counter_s[s[r]] == counter_t[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < ans[0]:
                    ans = [r - l + 1, l, r]
                counter_s[s[l]] -= 1
                if s[l] in counter_t and counter_s[s[l]] < counter_t[s[l]]:
                    have -= 1
                l += 1
        return "" if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]