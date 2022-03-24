'''
Created on Apr 19, 2019

@author: toni

Module that contains a set of functions to modify a file to successfully run
the file, display any return values, if any, and revert the file to its
original state.

CAUTION: always create a backup of the file, just in case the operations that
modify the file cause some unexpected modifications that alters the data of
the file in any unwanted way.
'''

import os


def run_file(filename):
    '''
    Run a file.

    filename -- string, name of the file with extension

    Prepends a file with a shebang, makes it executable, runs it, displays
    the result, removes the executable permission and shebang.
    '''
    print('Adding python interpreter path...')
    write_shebang(filename)
    print(f'Making {filename} executable...')
    make_executable(filename)
    print(f'Running file {filename}...\nResult:')
    run(filename)
    print(f'Removing {filename} executable permission...')
    remove_executable(filename)
    print('Removing python interpreter path...')
    remove_shebang(filename)
    print('Done!')


def write_shebang(filename):
    '''
    Read a file and add a path to the python interpreter to the first line.

    filename -- string, name of the file with extension
    '''
    with open(filename, 'r',
              encoding='utf-8') as original: data = original.read()
    with open(filename, 'w', encoding='utf-8') as modified:
        modified.write("#! /usr/local/bin/python3\n" + data)


def remove_shebang(filename):
    '''
    Read a file and remove path to the python interpreter from the first line.

    filename -- string, name of the file with extension
    '''
    with open(filename, 'r', encoding='utf-8') as original:
        data = original.readlines()
    with open(filename, 'w', encoding='utf-8') as modified:
        modified.write(''.join(data[1:]))


def make_executable(filename):
    """Make the file executable.

    filename -- string, name of the file with extension
    """
    cmd = 'chmod +x ' + filename
    return pipe(cmd)


def run(filename):
    '''Run the file.

    filename -- string, name of the file with extension
    '''
    cmd = './' + filename
    res, stat = pipe(cmd)
    print(res)  # display the result after running the file
    return res, stat


def remove_executable(filename):
    """Remove the executable permission.

    filename -- string, name of the file with extension
    """
    cmd = 'chmod -x ' + filename
    return pipe(cmd)


def pipe(cmd):
    """Run a command in a subprocess.

    cmd: string Unix command

    Returns: (res, stat), the output of the subprocess and the exit status.
    """
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def main():
    run_file('execution_time.py')


if __name__ == "__main__":
    main()
