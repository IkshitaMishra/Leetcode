class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        li = []
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if len(a) != 0 and len(b) != 0:
            if len(a) > len(b):
                b = str(b).zfill(len(a))
            if len(a) < len(b):
                a = str(a).zfill(len(b))
            carry = 0
            for j in range(len(a))[::-1]:
                if a[j] == '1' and b[j] == '1':
                    ans = 0 + carry
                    li.append(ans)
                    carry = 1
                else :
                    ans = int(a[j]) + int(b[j]) + carry
                    if ans == 2 or ans == 3:
                        ans  = 0
                        carry = 1
                    else:
                        carry = 0
                    li.append(ans)
            li = li[::-1]
            if carry == 1:
                li.insert(0,1)
            return "".join(str(i) for i in li)

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
            a = stringToString(line);
            line = next(lines)
            b = stringToString(line);
            
            ret = Solution().addBinary(a, b)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()