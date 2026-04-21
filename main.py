def flames_game(name1, name2):
    # 1. Clean the names (remove spaces and make lowercase)
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    # 2. Remove common characters between the pair of names
    list1 = list(name1)
    list2 = list(name2)
    
    for char in list1[:]:
        if char in list2:
            list1.remove(char)
            list2.remove(char)

    count = len(list1) + len(list2)

    # 3. FLAMES Logic
    # F = Friends, L = Love, A = Affection, M = Marriage, E = Enemy, S = Sibling
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Sister/Brother"]

    if count > 0:
        while len(flames) > 1:
            # Finding the index to remove using circular logic
            index = (count % len(flames)) - 1
            if index >= 0:
                # Split the list and rejoin to simulate circular removal
                right = flames[index + 1:]
                left = flames[:index]
                flames = right + left
            else:
                flames.pop(len(flames) - 1)
        
        return flames[0]
    else:
        return "Names are too similar! Try different names."

# This part allows the website to trigger the function
def start_game():
    # In a PyScript environment, we usually grab inputs from the HTML page
    # For now, you can test it locally in PyCharm with this:
    n1 = input("Enter first name: ")
    n2 = input("Enter second name: ")
    print(f"Relationship: {flames_game(n1, n2)}")

if __name__ == "__main__":
    start_game()
