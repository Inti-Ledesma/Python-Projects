from ma_apps import *
from ma_functions import *

system("cls")
lang_dict = get_language()

system("cls")
print(lang_dict["#welcome"])

option = -1

while(option != 0):
    msg = lang_dict["#menu"]
    err_msg = lang_dict["#menu_err"]
    option = is_numeric_in_range(msg, err_msg, (0,2))

    sel_app = lang_dict["#app_selected"]
    match option:
        case 1:
            sel_app += lang_dict["#app_01"] + "\n"
        case 2:
            sel_app += lang_dict["#app_02"] + "\n"

    system("cls")
    print(sel_app)
    match option:
        case 1:
            mad_libs_app(lang_dict)
        case 2:
            guess_the_number(lang_dict)
    
    system("cls")

print(lang_dict["#farewell"])
