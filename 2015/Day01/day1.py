def determine_floor(directions):
    floor = 0
    for c in directions:
        if c == '(':
            floor += 1
        else:
            floor -= 1
    
    return floor

def basement_index(directions):
    floor = 0
    for idx, c in enumerate(directions):
        if c == '(':
            floor += 1
        else:
            floor -= 1
        
        if floor < 0:
            return idx
    
    return -1

if __name__ == "__main__":
    # Read input into a list of lists - containing the calories for each elf
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    directions = lines[0]

    print(f"Part 1: {determine_floor(directions)}")
    print(f"Part 2: {basement_index(directions) + 1}")