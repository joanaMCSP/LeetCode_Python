class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        n = len(s)
        vowels = [x for x in s if self.isVowel(x)]
        indexes =[i for i in range(n) if self.isVowel(s[i])]
        vowels.reverse()

        for index, vowel in zip(indexes, vowels):
            result[index] = vowel
        return ''.join(result)

    def isVowel(self, letter):
        return letter in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} 
