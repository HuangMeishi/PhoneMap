


class Solution:
	def letterCombinations(self, digits : str):
		if not digits: return []
		
		phoneMap = {
			"2" : "abc",
			"3" : "def",
			"4" : "ghi",
			"5" : "jkl",
			"6" : "mno",
			"7" : "pqrs",
			"8" : "tuv",
			"9" : "wxyz"
			}
		def backtrace(combination, nextdigit):
			if len(nextdigit) == 0:
				res.append(combination)
			else:
				for letter in phoneMap[nextdigit[0]]:
					backtrace(combination + letter, nextdigit[1:])
		res = []
		backtrace('', digits)
		return res

if __name__ == '__main__':
	str = '23'
	res = Solution().letterCombinations(str)
	print(res)
	str = '9'
	print(Solution().letterCombinations(str))
	
				

