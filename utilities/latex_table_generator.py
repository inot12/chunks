'''
Created on Apr 17, 2019

@author: toni
'''


def table_generator(data_file, capt, label, filename='latex_table', r=2):
    '''
    Convert a set of data to a form used to generate latex tables.

    data_file -- string name of the file that contains the data
    capt, label -- strings describing the table
    filename -- string name of the file where the latex table will be saved
    r -- integer, represents the number of digits to be rounded down to

    You can choose to store the variable values in either columns or rows.
    '''

    checker = input('What format do you want?(column:c, row:r):')
    if checker == 'c':
        column_style_table(data_file, capt, label, filename, r)
    elif checker == 'r':
        row_style_table(data_file, capt, label, filename, r)
    else:
        raise ValueError('Input not properly defined. Enter either: c or r')


def column_style_table(data_file, capt, label, filename='latex_table', r=2):
    '''
    Convert a set of data to a form used to generate latex column tables.

    data_file -- string name of the file that contains the data
    capt, label -- strings describing the table
    filename -- string name of the file where the latex table will be saved
    r -- integer, represents the number of digits to be rounded down to
    '''
    data = read_data(data_file)
    # transpose the data so that m x n becomes n x m
    transdata = [[row[i] for row in data] for i in range(len(data[0]))]

    file = open(str(filename) + ".txt", "w", encoding='utf-8')
    file.write('\\begin{table}[H]\n'
               '\\centering\n'
               f'\\caption{{{capt}}}\n'
               # adjust automatically to the  number of expected columns
               '\\begin{tabular}{|c|' + 'c|' * len(data) + '}\n'
               '\\hline\n')

    for index in range(len(transdata)):
        file.write(str(index))
        for value in transdata[index]:
            file.write(" & " + str(round(float(value), r)))
        # the string "\\\\" denotes the \\ (end of the line sign)
        file.write("\\\\" + "\n\\hline\n")

    file.write('\\end{tabular}\n'
               f'\\label{{{label}}}\n'
               '\\end{table}')
    file.close()


def row_style_table(data_file, capt, label, filename='latex_table', r=2):
    '''
    Convert a set of data to a form used to generate latex row tables.

    data_file -- string name of the file that contains the data
    capt, label -- strings describing the table
    filename -- string name of the file where the latex table will be saved
    r -- integer, represents the number of digits to be rounded down to
    '''
    data = read_data(data_file)
    with open(str(filename) + '.txt', 'w', encoding='utf-8') as f:

        f.write('\\begin{table}[H]\n'
                '\\centering\n'
                f'\\caption{{{capt}}}\n'
                '\\begin{tabulary}{\\textwidth}{' +
                '|C' * len(data[0]) + '|}\n'
                '\\hline\n')

        for values in data:
            for index, value in enumerate(values):
                if index < (len(data[0]) - 1):
                    f.write("%s" % round(float(value), r) + " & ")
                else:
                    f.write("%s" % round(float(value), r) + "\\\\")
            f.write('\n\\hline\n')

        f.write('\\end{tabulary}\n'
                f'\\label{{{label}}}\n'
                '\\end{table}')


def read_data(data_file):
    '''
    Read a data set arranged in columns, each column separated by whitespace.

    data_file -- name of the file that contains the data

    returns:  a list of tuples containing strings
    '''
    with open(str(data_file) + '.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()

    wordlist = []
    for line in data:
        wordlist.append(line.split())

    return list(zip(*wordlist))


def main():
    data = read_data('Linearno_pomak_sila')  # testing read_data
    print(data, len(data[0]), sep='\n')  # testing data output

    # testing the transpose of the list
    t = [[row[i] for row in data] for i in range(len(data[0]))]
    print(t, len(t), sep='\n')

    # testing column style
    column_style_table('Linearno_pomak_sila', 'Testcapt', 'testlab',
                       'latex_table_column')

    # testing row style
    row_style_table('Linearno_pomak_sila', 'Testcapt', 'testlab',
                    'latex_table_row')

    table_generator('Linearno_pomak_sila', 'Placeholder caption',
                    'Placeholder label')


if __name__ == "__main__":
    main()
