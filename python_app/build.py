import os

if __name__ == '__main__':
    value = os.system('python setup.py build')
    if value == 1:
        value = os.system('python setup.py build')
    if value == 1:
        print('Cannot compile')
