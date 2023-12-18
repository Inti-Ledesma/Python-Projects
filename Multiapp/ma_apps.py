import ma_functions as maf
from random import randint
from os import system

def mad_libs_app(lang_dict:dict):
    '''
    Brief: This app asks the user for some words and then put them
    together on a short sentence
    
    Parameters:
        - lang_dict: A dictionary with every sentence used in the app
    '''
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
    '''
    Brief: This app asks for a range starting from 1, then it will give
    the user three attempts to guess the number between that range
    
    Parameters:
        - lang_dict: A dictionary with every sentence used in the app
    '''
    option = 1

    while option != 0:
        msg = lang_dict["#02_range"]
        err_msg = lang_dict["#02_range_err"]
        limit = maf.get_numeric_option_in_range(msg, err_msg, (1,10000))
        rand_num = randint(1, limit)

        num_sel = 0
        tries = 3
        while num_sel != rand_num and tries > 0:
            msg:str = lang_dict["#02_guess"]
            msg = msg.replace("#1", str(limit))
            msg = msg.replace("#2", str(tries))

            num_sel = maf.get_numeric_option_in_range(msg, err_msg, (1,10000))
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

def rock_paper_scissors(lang_dict):
    '''
    Brief: This app it's the classic game "Rock, paper, scissors",
    the user competes with the CPU, the one that gains 3 points first wins
    
    Parameters:
        - lang_dict: A dictionary with every sentence used in the app
    '''
    option = 1
    elements = lang_dict["#03_elements"].split()

    while option != 0:
        user_score = 0
        cpu_score = 0
        while user_score < 3 and cpu_score < 3:
            scores = lang_dict["#03_scores"].replace("#1",str(user_score))
            scores = scores.replace("#2",str(cpu_score))
            print(scores)
            msg = lang_dict["#03_choice"]
            err_msg = lang_dict["#03_choice_err"] + scores
            user_choice = maf.get_numeric_option_in_range(msg, err_msg, (1,3)) - 1
            cpu_choice = randint(0,2)
            print(elements[user_choice], "vs", elements[cpu_choice])
            result = "win"

            if user_choice == cpu_choice:
                result = "tie"
            else:
                match user_choice:
                    case 0:
                        if cpu_choice == 1:
                            result = "lose"
                    case 1:
                        if cpu_choice == 2:
                            result = "lose"
                    case 2:
                        if cpu_choice == 0:
                            result = "lose"
            
            match result:
                case "win":
                    user_score += 1
                case "lose":
                    cpu_score += 1

            print(lang_dict[f"#03_{result}_point"])
            
            input(lang_dict["#03_continue"])
            system("cls")
        
        if user_score > cpu_score:
            print(lang_dict[f"#03_win_match"])
        else:
            print(lang_dict[f"#03_lose_match"])

        option = maf.try_again(lang_dict)