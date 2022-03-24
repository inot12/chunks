'''
Created on Apr 11, 2019

@author: toni

This program is part of an exercise in
Think Python: An Introduction to Software Design
Allen B. Downey

WARNING: this program contains a NASTY bug.  I put
it there on purpose as a debugging exercise, but
you DO NOT want to emulate this example!
'''


class Kangaroo():
    '''This is a kangaroo.

    attributes: pouch_contentts
    '''

    def __init__(self, pouch_contents=[]):
        self.pouch_contents = pouch_contents

    def __str__(self):
        return '{}, {}'.format(object.__str__(self), self.pouch_contents)

    def put_in_pouch(self, *args):
        self.pouch_contents.append(*args)


class KangarooDowney():
    """A Kangaroo is a marsupial."""

    def __init__(self, contents=[]):
        """initialize the pouch contents; the default value is
        an empty list"""
        self.pouch_contents = contents

    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [object.__str__(self) + ' with pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)


def main():
    print('Kangaroo class')
    kanga = Kangaroo(['a', 3])
    roo = Kangaroo()
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)

    print('KangarooDowney class')
    kanga = KangarooDowney()
    roo = KangarooDowney()
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('car keys')
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)

"""If you run this program as it is, it seems to work.
To see the problem, trying printing roo.
The problem is the default value for contents.
Default values get evaluated ONCE, when the function
is defined; they don't get evaluated again when the
function is called.
After that, every Kangaroo that gets the default
value gets a reference to THE SAME list.  If any
Kangaroo modifies this shared list, they all see
the change.
We can define a function or method utilities.
This example shows an idiomatic way to avoid this problem."""


def utilities(self, contents=None):
    """
    The default value of contents is None.  When
    utilities runs, it checks the value of contents and,
    if necessary, creates a new empty list. That way,
    every Kangaroo that gets the default value gets a
    reference to a different list.

    As a general rule, you should avoid using a mutable
    objects as a default value, unless you really know
    what you are doing."""
    if contents is None:
        contents = []
    self.pouch_contents = contents


if __name__ == "__main__":
    main()
