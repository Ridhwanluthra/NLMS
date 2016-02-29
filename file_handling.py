# In below statements, write 'a' for appending in file; 'w' for just writing in file; 'r' for just reading the file

file_name='coords.txt'
digit=8
x=2
y=2
def write_in_file(digit, x, y):
    lst=[digit, x, y]
    with open(file_name,'a') as myfile:
        myfile.write(",".join(map(str, lst)))
        myfile.write('\n')

def getcoords(digit):
    digit_as_char=str(digit)
    f=open(file_name, 'r')
    list_of_lines=f.readlines()
    for j in range (len(list_of_lines)):
        if list_of_lines[j][0]==digit_as_char:
            i=list_of_lines[j][2]
            x_found=''
            counter=2;
            while(i!=","):
                x_found+=i
                counter+=1
                i=list_of_lines[j][counter]
            else:
                y_found=''
                counter+=1
                i=list_of_lines[j][counter]
                while(i!='\n'):
                    y_found+=i
                    counter+=1
                    i=list_of_lines[j][counter]
                return [int(x_found), int(y_found)]
    print ("Digit not found")
    return [-1]
def getdigit(x, y):
    x_as_str=str(x)
    y_as_str=str(y)
    f=open(file_name, 'r')
    list_of_lines=f.readlines()
    for j in range (len(list_of_lines)):
        i=list_of_lines[j][2]
        x_found=''
        counter=2;
        while(i!=","):
            x_found+=i
            counter+=1
            i=list_of_lines[j][counter]
        else:
            if x_found==x_as_str:
                y_found=''
                counter+=1
                i=list_of_lines[j][counter]
                while(i!='\n'):
                    y_found+=i
                    counter+=1
                    i=list_of_lines[j][counter]
                else:
                    if y_found==y_as_str:
                        return int(list_of_lines[j][0])
    print ("No number at this coordinate")
    return -1
