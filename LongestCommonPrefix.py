class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) != 0:
            leastprefix = min(strs, key=len)
            lenpre = len(leastprefix)
            rs=[]
            for a in range(0,lenpre):
                s= set([w[a] for w in strs])
                if len(s)==1:
                    rs.append(", ".join(s))
                else:
                    break  
            return ''.join([str(i) for i in rs])
        else:
            return ""

def stringToStringArray(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            strs = stringToStringArray(line)
            
            ret = Solution().longestCommonPrefix(strs)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()