
"""
*
* * Project name: Combinator
*
* * Purpose: The program saves every single character of a string,
*          After it, the program will make every single possible combination to make the same word.
*          The program also makes capitalized and non-capitalized versions of the string
*
* * Date of creation: 10/06/2022
*
* * Created by MiceX
*
"""

# Modules #
import itertools
import time


# Basically to fnd the amount of items we can just do 2^^n
def get_items(obj):
    count = 0
    for i in obj:
        count += 1

    return f"\n[!] There are : {count} items"


def combinator(**dic):
    """
    *
    * * In: 1) A dictionary with lower case and upper case letter of a specific string
    *       2) A string which is the original string
    *
    * * Out: A tuple which contains every single combination
    *
    """

    result = map(''.join, itertools.product(*zip(dic["string"].upper(), dic["string"].lower())))

    if dic["save"] == "file":
        with open("output.txt", 'w') as fd:
            result = list(result)
            print(get_items(result))

            fd.write("\n".join(result))

    elif dic["save"] == "set":
        print("\n                         RESULT\n_____________________________________________________\n")
        result = set(result)
        print(result)
        print(get_items(result))

    elif dic["save"] == "tuple":
        print("\n                         RESULT\n_____________________________________________________\n")
        result = tuple(result)
        print(result)
        print(get_items(result))

    elif dic["save"] == "list":
        print("\n                         RESULT\n_____________________________________________________\n")
        result = list(result)
        print(result)
        print(get_items(result))

    else:
        print("[-] No such save option")


"""
*
* * When starting the program you will be asked multiple questions which the program depends on.
*
* *  There are a few ways for the result to be saved, as a file - output.txt or as a set/tuple/list.
*
"""

if __name__ == "__main__":
    string = input("[!] Insert your string >>> ")
    save = input("[!] What save option? file/set/tuple/list? >>> ")

    start = time.time()
    combinator(string=string, save=save)
    print(f"\n[!] It took {time.time()-start} seconds")



