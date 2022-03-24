'''
Created on Apr 5, 2019

@author: toni
'''

import glob
# import magic
import os


def sbe1(mydir):
    os.chdir(mydir)
    for file in glob.glob("*.txt"):
        print(file)


def sbe2(mydir):
    for file in os.listdir(mydir):
        if file.endswith(".txt"):
            print(os.path.join(mydir, file))


def sbe3(mydir):
    for root, dirs, files in os.walk(mydir):
        for file in files:
            if file.endswith(".txt"):
                print(os.path.join(root, file))

# def sb_file_type(mydir):
#     for root, dirs, files in os.walk(mydir):
#         os.chdir(root)
#         for file in files:
#             if magic.from_file(file).split(',')[0] ==\
#              'ASCII text' or 'UTF-8 Unicode text':
#                 print(file)


def main():
    sbe1('./')
    sbe2('./')
    sbe3('./')
    # sb_file_type('./')


if __name__ == "__main__":
    main()
