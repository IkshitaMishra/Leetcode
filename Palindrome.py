class Solution(object):
    def isPalindrome(self, x):
        alist = map(str, str(x))
        if alist == alist[::-1]:
            return True
        else:
            return False

def stringToInt(input):
    return int(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = stringToInt(line)
            
            ret = Solution().isPalindrome(x)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()