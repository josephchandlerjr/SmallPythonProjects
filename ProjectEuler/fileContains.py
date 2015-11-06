import sys, glob


def getFiles(s):
    fnames = glob.glob('*.py')
    return [name for name in fnames if s in open(name, 'r').read()]
    


if __name__ == '__main__':
    string = sys.argv[1]
    print(getFiles(string))
