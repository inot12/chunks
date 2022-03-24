'''
Created on Apr 20, 2019

@author: toni
'''
import os


def image_generator(path, filename='latex_images.txt'):
    '''
    Search the path for images and generate latex figure input.

    path -- string
    filename -- name of the file where the input will be saved,
               default = 'latex_images.txt'
    '''
    files = os.listdir(path)

    with open(filename, 'w', encoding='utf-8') as out:
        for index, file in enumerate(files):
            out.write('\\begin{figure}[H]\n'
                      f'\\includegraphics[width=0.8\\textwidth]{{{file}}}\n'
                      '\\centering\n'
                      '\\caption{@}\n'
                      f'\\label{{fig:{index+1}}}\n'
                      '\\end{figure}\n\n')


def caption_images(captions, filename='latex_images.txt'):
    '''
    Read a file containing latex figure input code, and assign captions
    to the images.

    filename -- string, name of the file to be edited
    captions -- list of strings, contains the captions for the images
             -- len(list) = number of images
             -- note that you need to know the order of the images and
                define a list manually so that every caption describes
                the appropriate image
    '''
    with open(filename, 'r', encoding='utf-8') as original:
        data = original.read()
        data = data.split('\n')

        check = 0
        for line in data:
            if line.startswith('\\begin'):
                check += 1
        assert check == len(captions), \
            'Number of captions is not equal to the number of figures.'

        counter = 0
        new_data = []
        for line in data:
            if line.startswith('\\caption'):
                line = line.replace('@', captions[counter])
                counter += 1
            new_data.append(line)

    data = '\n'.join(new_data)
    with open(filename, 'w', encoding='utf-8') as modified:
        modified.write(data)


def main():
    image_generator(
        '/home/inot/mystuff/THREAD/research_modular/images'
    )
    # image_generator('/home/toni/Desktop/my_stuff/studium/projectMT/'
    #                 'master_thesis/images')
    # ordered_captions = ['Deformed shape-cax4i',
    #                     'Deformed shape-cax4i plastic',
    #                     'Deformed shape-cax4r',
    #                     'Deformed shape-cax4r plastic',
    #                     'Deformed shape-cax4rsurf',
    #                     'Deformed shape-cax4rsurf plastic',
    #                     'Various defect shapes',
    #                     'Stages of deep drawing',
    #                     'Deep drawing process',
    #                     'FSB image',
    #                     'FSB logo',
    #                     'Deformed shape-s4',
    #                     'Deformed shape-s4 plastic',
    #                     'Deformed shape-s4surf',
    #                     'Deformed shape-s4surf plastic',
    #                     'Deformed shape-sax1',
    #                     'Deformed shape-sax1 plastic']
    # caption_images(ordered_captions)


if __name__ == '__main__':
    main()
