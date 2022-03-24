'''
Created on Mar 30, 2019

@author: toni
'''
import os
import shelve

import fruitful_functions as ff
from anagrams import signature

# import sys
# add the path to the source folder of a python module that you wish to import
# sys.path.insert(0, '../../statistics/source/combinatorics')
# import permutations


class Error(Exception):
    pass


class WriteError(Exception):
    pass


def file_walker():
    '''Traverse the current directory and print the absolute path for all
    files in cwd.

    os.walk returns the absolute path, a list of directories in the
    current directory, and a list of files in the current directory.'''
    for root, dirs, files in os.walk(os.getcwd()):
        for filename in files:
            print(os.path.join(root, filename))


def sed(pattern, replacement, infile, outfile):
    '''Modify a file by replacing the specified pattern with a new pattern and
    save the changes to a copy of the original file.

    Should be integrated with a function that changes to a desired directory.
    '''
    in_lines = []
    try:
        with open(infile, encoding='utf-8') as f:
            for line in f:
                in_lines.append(line)
    except FileNotFoundError:
        print('Original file not in cwd!')

    targets = {pattern: replacement}
    out_lines = []
    try:
        with open(outfile, encoding='utf-8') as out:
            for line in in_lines:
                for tar, rep in targets.items():
                    line = line.replace(tar, rep)
                    out_lines.append(line)
    except ValueError:
        print('Pattern to be replaced not in the original file!')

    try:
        with open(outfile, 'w', encoding='utf-8') as out:
            for line in out_lines:
                out.write(line)
    except WriteError:
        print('Cannot write the file. Permission denied!')


def sed2(pattern, replace, source, dest):
    """Read a source file, replace the pattern and write to the destination
    file.

    In each line, replace pattern with replace.

    pattern -- string
    replace -- string
    source -- string, filename
    dest -- string, filename
    """
    try:
        fin = open(source, 'r', encoding='utf-8')
        fout = open(dest, 'w', encoding='utf-8')

        for line in fin:
            line = line.replace(pattern, replace)
            fout.write(line)

        fin.close()
        fout.close()
    except Error:
        print('Something went wrong.')


def sed3(pattern, replace, source, dest):
    '''Read a file, replace the pattern and write the changes to a new file.

    pattern -- string
    replace -- string
    source -- string, filename
    dest -- string, filename
    '''
    try:
        with open(source) as infile, open(dest, 'w') as outfile:
            for line in infile:
                line = line.replace(pattern, replace)
                outfile.write(line)
    except Error:
        print('Error: either specified source file not in cwd! or '
              'Destination file write permission denied')


def store_anagrams(d, dest):
    '''Store a dictionary mapping to a file.

    d -- dictionary, key -> list of strings
    dest - string filename
    '''
    s = ', '
    with open(dest, 'w', encoding='utf-8') as out:
        for key, value in d.items():
            if len(value) > 1:
                line = s.join(value)
                line = key + '\t' + line + '\n'
                out.write(line)


def shelve_store_anagrams(d, dest):
    shelf = shelve.open(dest, 'c')

    for key, anagram_list in d.items():
        shelf[key] = anagram_list

    shelf.close()


def store_anagrams_down(filename, ad):
    """Store the anagrams in ad to a shelf.

    filename -- string, name of shelf
    ad -- dictionary, maps strings to list of anagrams

    A shelf is a file that stores data in encrypted form.
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in ad.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    """Look up a word in a shelf and return a list of its anagrams.

    filename: string, name of shelf
    word: string, word to look up
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


def join_strings(seq, delimiter):
    '''Join a sequence of strings with a delimiter.

    seq -- a sequence of strings
    delimiter -- string
    '''
    item = delimiter.join(seq)
    return item


def pipe_commands(command):
    '''Use a shell command to do something.

    command -- a shell command in string format
    '''
    smt = os.popen(command)
    disp = smt.read()
    smt.close()
    print(disp)


def linecount(filename):
    count = 0
    for line in open(filename, encoding='utf-8'):
        count += 1
    return count


def main():
    file_walker()
    print(ff.duration(sed('ch', 'chapter', 'python_intro', 'copy_write_test')))
    print(ff.duration(sed2('ch', 'chapter', 'python_intro', 'intro_copy')))
    print(ff.duration(sed('python', 'c++', 'python_tips', 'tips1')))
    print(ff.duration(sed2('python', 'c++', 'python_tips', 'tips2')))
    print(ff.duration(sed3('hijgf', 'c++', 'python_tips', 'tips3')))
    print(linecount('file_writing.py'))
    print(__name__)


if __name__ == '__main__':
    main()
