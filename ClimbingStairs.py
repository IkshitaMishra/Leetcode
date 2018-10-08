class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d={0:0,1:1,2:2}
        for i in range(3,n+1):
            sum1=d.get(i-1) + d.get(i-2)
            d.update({i:sum1})
        return d.get(n)

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
            n = int(line);
            
            ret = Solution().climbStairs(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()