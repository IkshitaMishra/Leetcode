class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 0
        right = x
        if x > 1 :
            while left <= right:
                mid = int(left + (right-left)/2)
                if mid**2 <= x < (mid+1)**2:
                    return mid
                if x < mid**2:
                    right = mid
                if x > mid**2:
                    left = mid +1

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
            x = int(line);
            
            ret = Solution().mySqrt(x)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()