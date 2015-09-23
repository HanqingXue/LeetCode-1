


# More Pythonic Solution but same general idea
def groupAnagrams(strs):
    out = []
    hashTable = {}
    old = ["".join(sorted(word)) for word in strs]
    #print(old)
    for i in range(len(strs)):
        try:
            hashTable[old[i]].append(strs[i])
        except KeyError:
            hashTable[old[i]] = [strs[i]]
    #print(hashTable)
    
    for key, value in hashTable.items():
        out.append(value)
    
    out = [sorted(x) for x in out]
    out.sort()
    
    return out
    
A = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(A)
