class Solution:
    def strStr(self, haystack, needle):
        
        if needle in haystack:
            return haystack.find(needle) 
        else:
            return -1

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
            haystack = stringToString(line);
            line = next(lines)
            needle = stringToString(line);
            
            ret = Solution().strStr(haystack, needle)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()