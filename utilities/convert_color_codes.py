"""
Created on Jun 30, 2020

@author:toni
"""


def convert_color_codes(color):
    """
    Convert a decimal code to RGB.

    color -- tuple of integers; decimal color code
    Returns: list of integers; RGB color code
    """
    return [round(code_digit/255, 2) for code_digit in color]


def main():
    print(convert_color_codes((70, 130, 180)))


if __name__ == "__main__":
    main()
