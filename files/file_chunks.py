"""
Created on Apr 30, 2020

@author:toni
"""

import glob
import json
import os
import sys
from pathlib import Path

dirname = os.path.dirname(__file__)
# print(sys.path)
sys.path.insert(0, dirname)


def search_filesystem(path, pattern):
    """Search all files in path which match the pattern.

    path -- string, absolute path to directory being searched
    pattern -- e.g. '*.py'
    """
    for filename in Path(path).rglob(pattern):
        print(filename)


def abs_path(ext):
    """Find all files with .ext and return absolute path for each.

    ext -- string; e.g. 'txt', 'png', 'py'
    returns: list of absolute paths for found files"""
    return [os.path.realpath(f) for f in glob.glob(f'*.{ext}')]


def swap_dict_keys_and_values(d):
    """d -- dictionary"""
    return {value: key for key, value in d.items()}


def open_file(filename):
    """
    Open a file and handle the exception if file is not found.

    filename -- string; name of the file
    """
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
        file_read = True
    except FileNotFoundError:
        print(f'File "{filename}" not found!')
        # pass  # if you want to "fail silently"
        file_read = False
    else:
        print(contents)
    finally:
        if file_read:
            mussage = 'Read file operation successful!'
            print('\n\n{}\n{}'.format('-' * len(mussage), mussage))
        else:
            print('Read file operation not successful!')


def store_data(filename, data):
    """Store data to a .json file.

    filename -- string
    data -- contents of the file
    """
    with open(filename, 'w', encoding='utf-8') as f_obj:
        json.dump(data, f_obj)


def load_data(filename):
    """Store data to a .json file.

    filename -- string
    """
    with open(filename, 'r', encoding='utf-8') as f_obj:
        data = json.load(f_obj)

    print(data)


def greet_user():
    """Load the username, if it has been stored previously.
    Otherwise, prompt for the username and store it.
    """
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename, encoding='utf-8') as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w', encoding='utf-8') as f_obj:
        json.dump(username, f_obj)
    return username


def text_char_replacement(path, filename):
    '''
    Find all signs , (comma) and replaces them with . (dot).

    path -- string, where the file will be created
    filename -- string
    '''
    replacements = {',': '.'}
    lines = []

    with open(str(path) + str(filename) + '.txt', encoding='utf-8') as infile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            lines.append(line)

    with open(str(path) + str(filename) + '.txt',
              'w', encoding='utf-8') as outfile:
        for line in lines:
            outfile.write(line)


def main():
    open_file('file_writing.py')
    greet_user()
    print(abs_path('txt'))
    print(swap_dict_keys_and_values({"a": 1, "b": 2, "c": 3}))


if __name__ == "__main__":
    main()
