import os


def kgs_to_lbs(weight_to_be_converted):
    converted_weight = weight_to_be_converted * 2.20462
    print("Weight in Lbs: ")
    return round(converted_weight, 2)


def lbs_to_kgs(weight_to_be_converted):
    converted_weight = weight_to_be_converted * 0.453592
    print("Weight in Kgs: ")
    return round(converted_weight, 2)


print(
    """▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ███ █ ▄▄██▄██ ▄▄▄█ ████▄ ▄████ ▄▄▀█▀▄▄▀█ ▄▄▀█▀███▀█ ▄▄█ ▄▄▀█▄ ▄█ ▄▄█ ▄▄▀
██ █ █ █ ▄▄██ ▄█ █▄▀█ ▄▄ ██ █████ ████ ██ █ ██ ██ ▀ ██ ▄▄█ ▀▀▄██ ██ ▄▄█ ▀▀▄
██▄▀▄▀▄█▄▄▄█▄▄▄█▄▄▄▄█▄██▄██▄█████ ▀▀▄██▄▄██▄██▄███▄███▄▄▄█▄█▄▄██▄██▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"""
)

print("""
Chose conversion:
1. Kgs to Lbs
2. Lbs to Kgs
""")


while True:
    try:
        convesrion_type = int(input("Enter conversion number (1/2): "))
        if convesrion_type not in (1, 2):
            print("Not a valid input!")
            print()
        else:
            break

    except ValueError:
        print("Please provide a valid input!")
        print()
        continue


while True:
    try:
        weight_to_be_converted = int(input("Enter weight: "))
    except ValueError:
        print("Please provide a valid input!")
        print()
        continue
    else:
        break


if convesrion_type == 1:
    print(kgs_to_lbs(weight_to_be_converted=weight_to_be_converted))

elif convesrion_type == 2:
    print(lbs_to_kgs(weight_to_be_converted=weight_to_be_converted))
