class Solution(object):
    def twoSum(self, nums, target):
        a = list(nums)
        b = dict(enumerate(a))
        reslist =[]
        for key, val in b.items(): 
            res = target-val
            if res in b.values():
                index=[k for k,v in b.items() if v == res][0]
                if key != index:
                    reslist.append(key)
                    reslist.append(index)
                    break
        return reslist

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
            target = stringToInt(line)
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()