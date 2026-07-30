#------------------------------------
#-------Function Recursion-----------
#------------------------------------

# Test Word [ WWWoooorrrldd ] # print(x [1:])

def cleanWord(word):

    if len(word) == 1:

        return word
    
        print(f"print Start Function : {word}") # WWWoooorrrldd

    if word[0] == word[1]:

        print(f"print Before condition : {word}") # WWWoooorrrldd

        return cleanWord(word[1:]) # Recursion Function Call

        print(f"print Before Return : {word}") # WWWoooorrrldd

        return word[0] + cleanWord(word[1:]) # Recursion Function Call

    # Stash [ world ]
    print(cleanWord("WWWoooorrrldd")) # World