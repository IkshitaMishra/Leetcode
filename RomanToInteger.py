class Solution(object):
    def romanToInt(self, s):
        numdict =	{
          "I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000
        }
        inlist = map(str,s)
        res = {k:v for k,v in numdict.items()}
        outlist = map(res.get, inlist)
        print(outlist)
        rev = outlist[::-1]
        sum = rev[0]
        print(rev)
        for ind, val in enumerate(rev[1:], start=1):
            if rev[ind] >= rev[ind-1]:
                sum = sum + val
            else:
                sum = sum - val
        return sum

def stringToString(input):
    return input[1:-1].decode('string_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            
            ret = Solution().romanToInt(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()