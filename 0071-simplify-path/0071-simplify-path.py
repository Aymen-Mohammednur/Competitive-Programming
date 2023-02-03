class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for directory in path:
            if len(directory) == 0 or directory == ".":
                continue
            if directory == "..":
                if stack: 
                    stack.pop()
                continue
            stack.append(directory)
        return "/" + "/".join(stack)