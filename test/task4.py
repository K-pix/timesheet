import random
import string


def generate_password():

    capital_letters = string.ascii_uppercase
    small_letters = string.ascii_lowercase
    special_characters = "#.@!"
    numbers = "123456789"

    first_char = random.choice(capital_letters)
    second_char = random.choice(small_letters)
    third_char = random.choice(special_characters)
    fourth_char = random.choice(numbers)

    rem = int(input("ENTER the length of password  you want :"))
    if rem >= 6 and rem <= 16:
        remaining_length = rem - 4

        all_characters = (
            string.ascii_letters + string.digits + special_characters
        )
        remaining_chars = "".join(
            random.choices(all_characters, k=remaining_length)
        )

        password = (
            first_char
            + second_char
            + third_char
            + fourth_char
            + remaining_chars
        )

    return password
    # else:
    #  print("out of range please enter length in rage")


if __name__ == "__main__":
    print(generate_password())
