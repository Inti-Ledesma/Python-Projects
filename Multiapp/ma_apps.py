import ma_functions as maf
from os import system
from random import randint

def mad_libs_app(lang_dict:dict):
    option = 1

    while option != 0:
        colour = input(lang_dict["#01_enter_colour"])
        adjective = input(lang_dict["#01_enter_adj"])
        noun = input(lang_dict["#01_enter_noun"])

        phrase:str = lang_dict["#01_phrase"]
        phrase = phrase.replace("#1",noun)
        phrase = phrase.replace("#2",colour)
        phrase = phrase.replace("#3",adjective)

        print(phrase)

        option = maf.try_again(lang_dict)

def guess_the_number(lang_dict:dict):
    option = 1

    while option != 0:
        msg = lang_dict["#02_range"]
        err_msg = lang_dict["#02_range_err"]
        limit = maf.is_numeric_in_range(msg, err_msg, (1,10000))
        rand_num = randint(1, limit)

        num_sel = 0
        tries = 3
        while num_sel != rand_num and tries > 0:
            msg:str = lang_dict["#02_guess"]
            msg = msg.replace("#1", str(limit))
            msg = msg.replace("#2", str(tries))

            num_sel = maf.is_numeric_in_range(msg, err_msg, (1,10000))
            tries -= 1

            if tries > 0 and num_sel != rand_num:
                if num_sel < rand_num:
                    print(lang_dict["#02_smaller_guess"])
                elif num_sel > rand_num:
                    print(lang_dict["#02_bigger_guess"])
            else:
                if tries > 0:
                    print(lang_dict["#02_right_guess"])
                else:
                    print(lang_dict["#02_wrong_guess"].replace
                            ("#1",str(rand_num)))

        option = maf.try_again(lang_dict)