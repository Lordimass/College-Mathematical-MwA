def int_input(printer:str = "", err_msg:str = None):
    invalid = True
    while invalid:
        val = input(printer)
        try:
            val = int(val)
            invalid = False
        except:
            if err_msg != None:
                print(err_msg)
    return val

def vertex_input():
    x = int_input("Enter the x coordinate of the point: ",
                   "Invalid integer")
    y = int_input("Enter the y coordinate of the point: ",
                   "Invalid integer")
    return (x,y)
    
def bool_input(printer = "", err_msg:str = None):
    invalid = True
    while invalid:
        val = input(printer).lower()
        if val in ["no", "n", "false", "0"]:
            return False
        elif val in ["yes", "y", "true", "1"]:
            return True
        
        if err_msg != None:
            print(err_msg)
