class Solution(object):
    def reverse(self, x):
        max = (2**31)-1
        min = (2**31) * -1 
        c=list(map(int,str(abs(x))))
        rev =c[::-1]
        ans = int("".join(map(str,rev)))
        
        if ans>=min and ans<=max:
            if x<0:
                return ans * -1
            else:
                return ans
        else:
            return 0

def stringToInt(input):
    return int(input)

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
            x = stringToInt(line)
            
            ret = Solution().reverse(x)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()