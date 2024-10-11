def flames_game():
    boy = input("Input Boy's name: ").lower().replace(" ", "")
    girl = input("Input Girl's name: ").lower().replace(" ", "")
    
    # Find common characters and calculate remaining total iterations
    common_chars = set(boy).intersection(set(girl))
    total_iter = len(boy) + len(girl) - len(common_chars)*2
    
    flames_list = ['F','L','A','M','E','S']
    
    while len(flames_list) > 1:
        eliminate_index = (total_iter - 1) % len(flames_list)
        print(f"Removing: {flames_list[eliminate_index]}")
        
        if eliminate_index == len(flames_list) - 1:
            flames_list = flames_list[:eliminate_index]
        elif eliminate_index == 0:
            flames_list = flames_list[eliminate_index + 1:]
        else:
            flames_list = flames_list[eliminate_index + 1:] + flames_list[:eliminate_index]
    
    result = flames_list[0]
    relationship_dict = {
        'F': 'Friends',
        'L': 'Love',
        'A': 'Affair',
        'M': 'Marriage',
        'E': 'Enemy',
        'S': 'Sibling'
    }
    
    print(f"The relationship between the two is: {relationship_dict[result]}")

# Call the game function
flames_game()
