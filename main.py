import PySimpleGUI as sg
import re
import hashlib


def hash(fname, algor):
    if algor == 'MD5':
        hashu = hashlib.md5()
    elif algor == 'SHA1':
        hashu = hashlib.sha1()
    elif algor == 'SHA256':
        hashu = hashlib.sha256()
    with open(fname) as handle:  # opening the file one line at a time for memory considerations
        for line in handle:
            hashu.update(line.encode(encoding='utf-8'))
    return hashu.hexdigest()


layout = [
    [sg.Text('data_collet.xlsx'), sg.InputText(), sg.FileBrowse()],
    [sg.Output(size=(88, 20))],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Machine Learning System', layout)
while True:
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        file1 = file2 = isitago = None
        if values[0]:
            if not file1 and file1 is not None:
                print('Error: File 1 path not valid.')
                isitago = 0
            elif not file2 and file2 is not None:
                print('Error: File 2 path not valid.')
                isitago = 0
            elif values[1] is not True and values[2] is not True and values[4] is not True:
                print('Error: Choose at least one type of Encryption Algorithm')
            elif isitago == 1:
                print('Info: Filepaths correctly defined.')
                algos = []  # algos to compare
                if values[1]:
                    algos.append('MD5')
                if values[2]:
                    algos.append('SHA1')
                if values[4]:
                    algos.append('SHA256')
                filepaths = [values[0], values[3]]  # files
                print('Info: File Comparison using:', algos)
                for algo in algos:
                    print(algo, ':')
                    print(filepaths[0], ':', hash(filepaths[0], algo))
                    print(filepaths[1], ':', hash(filepaths[1], algo))
                    if hash(filepaths[0], algo) == hash(filepaths[1], algo):
                        print('Files match for ', algo)
                    else:
                        print('Files do NOT match for ', algo)
        else:
            print('Please choose 2 files.')
window.close()
