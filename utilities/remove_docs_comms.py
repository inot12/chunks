"""
Created on Apr 20, 2019

@author: toni

Strip comments and docstrings from a file.
"""

import token
import tokenize


def do_file(fname):
    """ Run on just one file."""
    source = open(fname, encoding='utf-8')
    name, ext = fname.split('.')
    mod = open('.'.join([name + "_strip", ext]), "w", encoding='utf-8')

    prev_toktype = token.INDENT
    first_line = None
    last_lineno = -1
    last_col = 0

    tokgen = tokenize.generate_tokens(source.readline)
    for toktype, ttext, (slineno, scol), (elineno, ecol), ltext in tokgen:
        if 0:  # Change to if 1 to see the tokens fly by.
            print("%10s %-14s %-20r %r" % (
                tokenize.tok_name.get(toktype, toktype),
                "%d.%d-%d.%d" % (slineno, scol, elineno, ecol),
                ttext, ltext
            ))
        if slineno > last_lineno:
            last_col = 0
        if scol > last_col:
            mod.write(" " * (scol - last_col))
        # if toktype == token.STRING and prev_toktype == token.INDENT:
        if toktype == token.STRING and (prev_toktype == token.INDENT or
                                        prev_toktype == token.NEWLINE):
            # Docstring
            pass  # mod.write("#--")
        elif toktype == tokenize.COMMENT:
            # Comment
            pass  # mod.write("##")
        else:
            mod.write(ttext)
        prev_toktype = toktype
        last_col = ecol
        last_lineno = elineno


if __name__ == "__main__":
    do_file('kangaroo.py')
    do_file('latex_table_generator.py')
