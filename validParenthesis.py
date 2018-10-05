class Solution(object):
    def isValid(self, s):
        inlist = map(str,s)
        a = {"(":")","[":"]","{":"}"}
        outlist = []
        for s in inlist:
            if s in a.keys():
                outlist.append(s)
            if s in a.values():
                if len(outlist) != 0:
                    if outlist[-1]  == "".join([k for k, v in a.items() if v == s]):
                        outlist.pop()
                    else:
                        break   
                else:
                    outlist.append(s)
                    break
            
        print(outlist)
        if len(outlist) == 0:
            return True
        else:
            return False

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            
            ret = Solution().isValid(s)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()