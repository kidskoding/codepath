# Input: A string containing open and closed parentheses
# Output: A boolean that determines if the string is valid parentheses/brackets

# 1. Create a dictionary containing the open and closing brackets, 
# where the keys will be closing brackets and the values will be the opening brackets
# 2. Create a stack that will track the ordering bracket types
# 3. Check if your current character is a key in the map (closing bracket) and if so, pop the top element from the stack
# 4. Check if stack is empty by end of the process and if so return True, otherwise False
# 
# Time: O(n)
# Space: O(n)

def is_valid_post_format(posts: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack: list[str] = []
    for post in posts:
        if post in bracket_map:
            if not stack:
                return False
            
            top = stack.pop()
            if bracket_map[post] != top:
                return False
        else:
            stack.append(post)

    return not stack
