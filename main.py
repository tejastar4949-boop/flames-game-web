def flames_game(name1, name2):
    # 1. Clean the names
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # 2. Remove common characters
    list1 = list(name1)
    list2 = list(name2)
    
    for char in list1[:]:
        if char in list2:
            list1.remove(char)
            list2.remove(char)

    count = len(list1) + len(list2)

    # 3. FLAMES Logic
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Sister/Brother"]

    if count > 0:
        while len(flames) > 1:
            index = (count % len(flames)) - 1
            if index >= 0:
                right = flames[index + 1:]
                left = flames[:index]
                flames = right + left
            else:
                flames.pop(len(flames) - 1)
        
        return flames[0]
    else:
        return "Names are too similar! Try different names."

# REMOVE the input() and print() lines from here for the web version.
# The index.html handles the inputs now!
