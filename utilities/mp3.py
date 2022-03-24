'''
Created on Apr 4, 2019

@author: toni
'''
import os


def search_by_ext(root, extension):
    """Search all the files within root with the specified extension.

    root -- string, path
    extension -- string, e.g. .pdf, .txt, .mp3
    """
    checksums = []
    os.chdir(root)
    rename(root)  # rename any irregular file names first
    denote_output('The absolute path to each file:')
    for abspath, directories, files in os.walk(root):
        for filename in files:
            if filename.endswith(extension):
                print(os.path.join(abspath, filename))
                # ensure that md5sum finds the file
                if filename not in root:
                    os.chdir(abspath)
                checksums.append(checksum(filename))
    denote_output('\nThe duplicate items are:')
    duplicate_items(compare_sum(checksums))


def checksum(file):
    """Check the md5sum of a file and return its checksum value as a tuple of
    filename and checksum value.

    file -- string, e.g. checksum('my_file.ext')
    """
    try:
        command = 'md5sum ' + str(file)
        check = os.popen(command)
        # return the hash value and the filename
        disp = check.read()
        chars = disp.split()
        chars_tuple = (chars[-1], chars[0])
        return chars_tuple
    except FileNotFoundError:
        print('Error: File not found!')


def compare_sum(checksums):
    """Take a list of tuple checksums and store them to a dictionary.

    All files with the same checksum will be in a list that is the value of
    the key checksum.
    """
    d = dict()
    for filename, hashval in checksums:
        if hashval not in d:
            d[hashval] = [filename]
        else:
            d[hashval].append(filename)
    return d


def duplicate_items(d):
    """Check for duplicate items in a dictionary.

    d -- dictionary, keys: checksums, values: files"""
    c = 0
    for value in d.values():
        if len(value) > 1:
            c += 1
            print(value)
    if c == 0:
        print('None')


def rename(root):
    """Rename files with irregular names."""
    denote_output('The following files have been renamed:')
    for abspath, dirs, filenames in os.walk(root):
        to_write = ['root == %s\n' % abspath]
        for filename in filenames:
            newname = filename.replace(" ", "_")
            tu = (os.path.join(abspath, filename),
                  os.path.join(abspath, newname))
            if tu[0] != tu[-1]:
                to_write.append('%s --> %s\n' % tu)
            os.rename(*tu)
        print('\n'.join(to_write))


def rename_file(root, filename):
    """Rename a file in root if it contains spaces ' '."""
    newname = filename.replace(" ", "_")
    tu = (os.path.join(root, filename), os.path.join(root, newname))
    os.rename(*tu)


def file_rename(root):
    """Search all directories and files in root rename them.

    path -- string, the directory to be searched

    This function will rename all files that contain spaces in them.
    e.g. 'my random file.ext' will become 'my_random_file.ext'.
    """
    for f in os.listdir(root):
        r = f.replace(" ", "_")
        if r != f:
            os.rename(f, r)


def denote_output(out):
    """Print the output string underlined with =."""
    print('%s \n%s \n' % (out, '=' * len(out.lstrip())))


def main():
    print(os.getcwd())
    search_by_ext(os.getcwd(), '.txt')


if __name__ == "__main__":
    main()
