# In below statements, write 'a' for appending in file; 'w' for just writing in file; 'r' for just reading the file

file_name='coords.txt'
def write_in_file(digit, x, y):
    lst=[digit, x, y]
    with open(file_name,'a') as myfile:
        myfile.write("".join(map(str, lst)))

def getcoords(digit):
    digit_as_char=str(digit)
    f=open(file_name, 'r')
    list_of_lines=f.readlines()
    for i in range (len(list_of_lines)):
        if list_of_lines[i][0]==digit_as_char:
            return [list_of_lines[i][1], list_of_lines[i][2]]
            pass
        else:
            print "Digit not found"
            return [-1]
def getdigit(x, y):
    x_as_str=str(x)
    y_as_str=str(y)
    f=open(file_name, 'r')
    list_of_lines=f.readlines()
    for i in range (len(list_of_lines)):
        if list_of_lines[i][1]==x_as_str and list_of_lines[i][2]==y_as_str:
            return digit
        else:
            print "No number at this coordinate"
            return -1
