"""
Created on Oct 28, 2020

@author:toni
"""

import os
import textwrap as tw


def limit_line_length(mydir, col=79, ext='.txt', mod='wrapped_'):
    """Search files by extension and limit the file's maximum line length.

    mydir -- string, absolute path of the starting directory
    col -- integer, line length limit
    ext -- string, extension of ALL files that will be wrapped
    mod -- string, name modifier for wrapped files

    returns: wrapped files with name mod+file
    """
    for root, dirs, files in os.walk(mydir):
        os.chdir(root)

        for file in files:
            if file.endswith(ext):
                if file.startswith(mod):
                    continue  # skip wrapped files
                else:
                    lines = []

                    with open(file, 'r', encoding='utf-8') as f:
                        for line in f:
                            if len(line) <= col - 1:
                                lines.append(line)
                            else:
                                wrapped = tw.wrap(line, width=col)
                                # wrapped lines are a list of lines
                                # join by \n to create a string and add \n to
                                # the end of the string to get desired output
                                lines.append('\n'.join(wrapped) + '\n')

                with open(mod + file, 'w', encoding='utf-8') as wf:
                    wf.write(''.join(lines))

    os.chdir(mydir)


def main():
    path = '/home/inot/mystuff/python/my_notes'
    limit_line_length(path)


if __name__ == "__main__":
    main()
