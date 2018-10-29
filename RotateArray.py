class Solution(object):
    

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        if k < n:
            k = k
        else:
            k = k%n
        temp = nums[n-k:n]
        for i in range(len(nums)):
            nums[n-1-i] = nums[n-k-i-1]
        for j in range(k):
            nums[j] = temp[j]
        print(nums)

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            line = lines.next()
            k = stringToInt(line)
            
            ret = Solution().rotate(nums, k)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()