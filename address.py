#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Dec 1, 2022
# A program the calculates the volume of a sphere.

# Formats the information to return back to main
def format_address(
    full_name, sheet_num, sheet_name_ty, city, province, postal, apart_num=None
):
    return_info = full_name
    if apart_num != None:
        # If the user lives in an apartment
        return_info = (
            full_name
            + "\n"
            + apart_num
            + " - "
            + sheet_num
            + " "
            + sheet_name_ty
            + " \n"
            + city
            + " "
            + province
            + " "
            + postal
        )
    # if the user doesn't live in a apartment
    else:
        return_info = (
            full_name
            + "\n"
            + sheet_num
            + " "
            + sheet_name_ty
            + " \n"
            + city
            + " "
            + province
            + " "
            + postal
        )

    return return_info


def main():
    apart_num = None

    # Inputs needed to get mailing address
    full_name = input("Enter your full legal name: ")
    question = input("Do you live in an apartment (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apart_num = input("Enter your apartment number: ")
    sheet_num = input("Enter your sheet number: ")
    sheet_name_ty = input("Enter your sheet type (Main...): ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")
    postal = input("Enter your postal code: ")
    print("")

    # Makes all the information upper case
    if apart_num != None:
        info = format_address(
            full_name, sheet_num, sheet_name_ty, city, province, postal, apart_num
        )
    else:
        info = format_address(
            full_name, sheet_num, sheet_name_ty, city, province, postal
        )
    info_caps = info.upper()
    # output
    print(info_caps)


if __name__ == "__main__":
    main()
