#User function Template for python3
class Solution:
	def addBinary(self, A, B):
	    carry = 0
        result = []
        a = list(A)
        b = list(B)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result.append(str(carry % 2))
            carry //= 2

        while result[-1] == '0':
            result.pop()
        result.reverse()
        return ''.join(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a,b = input().split(" ")
		ob = Solution()
		answer = ob.addBinary(a,b)
		
		print(answer)


# } Driver Code Ends