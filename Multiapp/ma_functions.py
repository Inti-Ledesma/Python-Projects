from os import system

def get_language():
    '''
    Brief: It will ask the user to select a language (Spanish or english)
    
    return:
        - lang_dict: A dictionary with every sentence used in the program
    '''
    msg = "Please, select a language:\n1. Español\n2. English\nOption: "
    err_msg = "Inexistent option, try again\n"
    lang = get_numeric_option_in_range(msg, err_msg, (1,2))
    match lang:
        case 1:
            lang = "es"
        case 2:
            lang = "en"

    path = f"Multiapp/lang/{lang}.txt"
    lang_dict = {}

    with open(path,"r",encoding="utf8") as f:
        for line in f:
            line = line.strip("\n").lstrip('"').rstrip('"')
            line = line.split('":"')
            line = [i.replace("\\n","\n") for i in line]

            lang_dict[line[0]] = line[1]
    
    return lang_dict

def get_numeric_option_in_range(msg:str, err_msg:str, range:tuple):
    '''
    Brief: It receives an input from the user determining if it's numeric
    and it's between a given range
    
    Parameters:
        - msg: The message that will be shown to the user through the input
        - err_msg: It will be shown in case the user doesn't enter a number
        or it's not between the given range
        - range: This tuple that will determine the minimum and maximum
        number possible for the user to input

    return:
        - option: The integer that the user entered
    '''
    option = input(msg)

    while (not option.isnumeric() or int(option) < range[0]
        or int(option) > range[1]):
        system("cls")
        print(err_msg)
        option = input(msg)
    
    system("cls")

    return int(option)

def try_again(lang_dict):
    '''
    Brief: A basic function to ask the user if wants to try again given
    two options: 1. Yes or 0. No
    
    Parameters:
        - lang_dict: Given to use the right sentences on the language
        selected

    return:
        - option: The option selected by the user
    '''
    msg = lang_dict["#try_again"]
    err_msg = lang_dict["#try_again_err"]
    option = get_numeric_option_in_range(msg, err_msg, (0,1))

    return option
