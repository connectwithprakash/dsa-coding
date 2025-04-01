"First try"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a, len_b = len(a), len(b)
        min_len = min(len_a, len_b)
        result = []
        carry = False
        for idx in range(-1, -min_len - 1, -1):
            if carry:
                # One of them is a 1
                if a[idx] != b[idx]:
                    carry = True
                    result.append("0")
                # both are "1"
                elif a[idx] == "1":
                    carry = True
                    result.append("1")
                # Both are "0"
                else:
                    carry = False
                    result.append("1")
            else:
                # One of them is a 1
                if a[idx] != b[idx]:
                    carry = False
                    result.append("1")
                # both are "1"
                elif a[idx] == "1":
                    carry = True
                    result.append("0")
                # Both are "0"
                else:
                    carry = False
                    result.append("0")
        if len_a > len_b:
            for jdx in range(idx - 1, -len_a - 1, -1):
                if carry:
                    if a[jdx] == "1":
                        result.append("0")
                        carry = True
                    else:
                        result.append("1")
                        carry = False
                else:
                    result.append(a[jdx])
        elif len_a < len_b:
            print(f"inside len b {b} > {list(range(idx, -len_b, -1))}")
            for jdx in range(idx - 1, -len_b - 1, -1):
                print(b, jdx, b[jdx])
                if carry:
                    print("inside b carry")
                    if b[jdx] == "1":
                        result.append("0")
                        carry = True
                    else:
                        result.append("1")
                        carry = False
                else:
                    print(f"no carry {b[jdx]}")
                    result.append(b[jdx])
                    carry = False
        if carry:
            result.append("1")
        return "".join(result[::-1])
