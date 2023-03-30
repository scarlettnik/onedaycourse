def check(s: str):
    br = '(){}[]'
    opening, closing = zip(*[(br[i], br[i+1]) for i in range(0, len(br), 2)])
    stack = []
    for i in range(len(s)):
        if s[i] in opening:
            stack.append((opening.index(s[i]), i + 1))
        elif s[i] in closing:
            if not stack or closing.index(s[i]) != stack.pop()[0]:
                return i + 1
    return stack.pop()[1] if stack else 'Success'
print(check(input()))
