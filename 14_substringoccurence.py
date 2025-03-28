import re
def longest_prefix(strs):
    l = len(strs[0])

    for i in range(1,len(strs)):
        length = min(l,len(strs[i]))
        while length > 0 and strs[0][0:length]!=strs[i][0:length]:
            length -= 1
            if length == 0:
                return "No common prefix"
    return strs[0][0:length]

def longest_prefix_regex(str):
    if not str:
        return "no string"
    
    prefix = str[0]
    for word in str[1:]:
        while not re.match(f"^{prefix}",word):
            prefix = prefix[:-1]
            if not prefix:
                return "No common prefix"
    return prefix


strs1 = ["red", "read", "redbull","required"]
strs = ["float", "flowing", "flown","flower", "flow"]
print(longest_prefix(strs))
print(longest_prefix_regex(strs))