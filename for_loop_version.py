def get_starting_number():
    """
    This function asks the user how many bottles of beer on the wall they want to start singing with, 
    e.g. "How many bottles of beer on the wall?" 

    The function asks this question as many times as necessary until the user enters a valid response, 
    which is considered to be any integer 1 or greater. 

    The function then returns the integer equivalent of the value the user entered. 

    The code for this function can be the same for all three versions of the program, 
    but must be copied into each file.
    """
    while True:
        num_bottles = input("How many bottles of beer on the wall? ")
        if num_bottles.isdigit() and int(num_bottles) >= 1:
            return int(num_bottles)
        

def sing(bottle_num):
    """
    This function takes an argument specifying how many bottles of beer to start with, 
    and then outputs the lyrics to the song, starting from that number of bottles.
    """
    for num in range(bottle_num, 0, -1):
        if num > 2:
            print(f"{num} bottles of beer on the wall, {num} bottles of beer.\nTake one down, pass it around, {num - 1} bottles of beer on the wall.\n")
        elif num == 2:
            print(f"2 bottles of beer on the wall, 2 bottles of beer.\nTake one down, pass it around, 1 bottle of beer on the wall.\n")
        elif num == 1:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!\n")
