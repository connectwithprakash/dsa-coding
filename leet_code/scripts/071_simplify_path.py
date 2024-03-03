class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for path_split in path:
            if (path_split == "") or (path_split == "."):
                continue
            elif (path_split == ".."):
                if len(stack):
                    stack.pop()
            else:
                stack.append(path_split)
        return "/" + "/".join(stack)

