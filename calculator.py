#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 4, 2023
# This program is a calculator using basic operations.


def calculator(num_one, num_two, sign):
    if sign == "+":
        answer = num_one + num_two
    elif sign == "-":
        answer = num_one - num_two
    elif sign == "/":
        answer = num_one / num_two
    elif sign == "*":
        answer = num_one * num_two
    else:
        answer = num_one % num_two
    return answer


def main():
    # introduce program to user
    print("This program is a calculator and uses basic operations.")

    # get user number and sign
    user_num_one = input("Please enter a number: ")
    user_num_two = input("Please enter a second number: ")
    user_sign = input("Please enter a sign (+, -, *, /, or %): ")

    # try casting first input to a float
    try:
        num_one_float = float(user_num_one)

        # try casting second input into a float
        try:
            num_two_float = float(user_num_two)

            if (user_sign == "+") or (user_sign == "-") or (user_sign == "/") or (user_sign =="%") or (user_sign == "*"):

                # call function
                calc_answer = calculator(num_one_float, num_two_float, user_sign)

                # display answer
                print(
                    "{} {} {} = {:.2f}".format(
                        num_one_float, user_sign, num_two_float, calc_answer
                    )
                )

            # tell user if invalid sign input
            else:
                print("{} is not a valid sign".format(user_sign))

        # catch invalid inputs for second number
        except Exception:
            print("{} is not a valid number".format(user_num_two))

    # catch invalid inputs for first number
    except Exception:
        print("{} is not a valid number.".format(user_num_one))


if __name__ == "__main__":
    main()
