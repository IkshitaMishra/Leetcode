class Solution:
    def lengthOfLastWord(self, s):
        
        li = list(filter(None,s.split(" ")))
        if len(li) == 0:
            return 0
        else: 
            return len(li[len(li)-1])

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().lengthOfLastWord(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()