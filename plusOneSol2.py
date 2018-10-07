class Solution:
    def plusOne(self, digits):
        
        if 9 in digits and len(set(digits)) > 1:
            print("a")
            if digits[-1] == 9:
                for i in range(1,len(digits))[::-1]:
                    if digits[i] == 9:
                        digits[i] = 0
                        if digits[i-1] != 9:
                            digits[i-1] = digits[i-1] + 1
                            return digits
                        
            if digits[-1] < 9:
                digits[-1] = digits[-1] + 1
                return digits
            
                
        if 9 in digits and len(set(digits)) == 1:
            print("b")
            for i in range(len(digits)):
                digits[i] = 0
            digits.insert(0,1)
            return digits
            
        if 9 not in digits:
            print("c")
            digits[-1] = digits[-1] +1 
            return digits

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            digits = stringToIntegerList(line);
            
            ret = Solution().plusOne(digits)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()