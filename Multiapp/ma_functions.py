from os import system

def get_language():
    msg = "Please, select a language:\n1. Español\n2. English\nOption: "
    lang = is_numeric_in_range(msg,"Inexistent option, try again\n",(1,2))
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

def is_numeric_in_range(msg:str, err_msg:str, limit:tuple):
    option = input(msg)

    while (not option.isnumeric() or int(option) < limit[0]
        or int(option) > limit[1]):
        system("cls")
        print(err_msg)
        option = input(msg)
    
    system("cls")

    return int(option)

def try_again(lang_dict):
    msg = lang_dict["#try_again"]
    err_msg = lang_dict["#try_again_err"]
    option = is_numeric_in_range(msg, err_msg, (0,1))

    return option
