''' 
Write a Python program named provinces.py that reads the contents of provinces.txt into a list and then modifies the list. Your program must do the following:

Open the provinces.txt file for reading.
Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
Print the entire list.
Remove the first element from the list.
Remove the last element from the list.
Replace all occurrences of "AB" in the list with "Alberta".
Count the number of elements that are "Alberta" and print that number.
'''

def main():
    # Read the contents of a text file named
    # provinces.txt into a list named provinces_list
    provinces_list = read('provinces.txt')
    # As a debugging aid, print the entire list.
    print(provinces_list)
    
    # Remove the first element from the list.
    provinces_list.pop(0)
    # print(provinces_list)
    
    # Remove the last element from the list.
    provinces_list.pop()
    
    # Replace all occurrrences of "AB" with "Alberta".
    for i in range(len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'
    # print (provinces_list)
    
    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = provinces_list.count('Alberta')
    print ()
    print (f"Alberta occurs {count} times in the modified list.")
    

def read(filename):
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []
    with open(filename, 'rt') as provinces:
        # Read the contents of the text
        # file one line at a time.
        for province_name in provinces:
            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = province_name.strip()
            # Append the clean line of text
            # onto the end of the list
            text_list.append(clean_line)           
    return text_list
    
   # Call main to start this program.
if __name__ == "__main__":
    main() 