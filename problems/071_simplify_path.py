# Attempt 1: Brute force
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_split = path.split("/")
        stack = []
        for i in range(len(path_split)):
            if path_split[i] == "..":
                if len(stack):
                    stack.pop()
            elif (path_split[i] == "") or (path_split[i] == "."):
                continue
            else:
                stack.append("/"+path_split[i])
        # stack = ["/"] + stack
        if len(stack):
            print(stack)
            return "".join(stack)
        else:
            return "/"
 
