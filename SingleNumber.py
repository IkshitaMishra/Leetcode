class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        li = []
        for i in nums:
            if i in li:
                li.remove(i)
            else:
                li.append(i)     
        return int(''.join(map(str,li)))

def stringToIntegerList(input):
    return json.loads(input)

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
            nums = stringToIntegerList(line)
            
            ret = Solution().singleNumber(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()