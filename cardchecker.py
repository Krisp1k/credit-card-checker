import re

def use_regex(input_text):
    pattern = re.compile(r"[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+-[A-Za-z0-9]+", re.IGNORECASE)
    if pattern.match(input_text):
        return True
    else:
        return False

def getSum(n):
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
  
def print_result(main_id, control_num, control_num_calculated, result):
    print("----------------------------------------------")
    print("K O N T R O L A   P L A T E B N Í   K A R T Y ")
    print("----------------------------------------------")
    print("______________________________________________")
    print("Kategorie platební karty        : " + str(main_id))
    #print("Značka karty                    : " + znacka)
    print("Kontrolní číslice zadaná        : " + str(control_num))
    print("Kontrolní číslice vypočtená     : " + str(control_num_calculated))
    print("Výsledek                        : " + result)
    print("----------------------------------------------")

def main():
    cards_dictionary = {
        0:"Mezinárodní organizace pro normalizaci (ISO)",
        1:"Letecká společnost",
        2:"Letecká společnost",
        3:"Cestování a zábava",
        4:"Bankovnictví - kreditní a debitní karty",
        5:"Bankovnictví - kreditní a debitní karty",
        6:"Merchandising a bankovnictví",
        7:"Ropný průmysl - tankovací karty",
        8:"Zdravotnictví a telekomunikace",
        9:"Statní organizace",
    }
    
    card_input = ""
    result = ""

    while True:
        card_input = input("Napište číslo karty ve formátu XXXX-XXXX-XXXX-XXXX (VISA nebo MASTERCARD only) :\n")
        if (use_regex(card_input)):
            break

    main_id = cards_dictionary[int(card_input[0])]
    control_num = card_input[len(card_input) - 1]
    list_card = list(card_input)

    nasobit = {
        0:list_card[0], 
        2:list_card[2], 
        5:list_card[5], 
        7:list_card[7], 
        10:list_card[10], 
        12:list_card[12], 
        15:list_card[15], 
        17:list_card[17]
    }

    for index, key in enumerate(nasobit):
        item = nasobit[key]
        vynasobeno = int(int(item) * 2)
        if (vynasobeno > 10):
            list_card[key] = getSum(vynasobeno)

    sum_of_all = 0

    for item in list_card:
        if (item != "-"):
            sum_of_all += int(item)

    num_str = repr(sum_of_all)
    last_digit_str = num_str[-1]
    last_digit = int(last_digit_str)
    control_num_calculated = 10 - last_digit

    if (int(control_num) == int(control_num_calculated)):
        result = "PLATNÁ"
    else:
        result = "FALEŠNÁ"

    print_result(main_id, control_num, control_num_calculated, result)

if __name__ == "__main__":
    main()