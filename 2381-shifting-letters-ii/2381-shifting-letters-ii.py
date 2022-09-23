class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        state = [0] * (len(s) + 1)
        for shift in shifts:
            if shift[2] == 0:
                state[shift[0]] -= 1
                state[shift[1] + 1] += 1
            else:
                state[shift[0]] += 1
                state[shift[1] + 1] -= 1
        for i in range(1, len(state)):
            state[i] = state[i - 1] + state[i]
        s = list(s)
        for i in range(len(s)):
            s[i] = chr((((ord(s[i]) + state[i]) - 97) % 26) + 97)
        return "".join(s)