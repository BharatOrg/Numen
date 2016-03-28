import xlwt
from optparse import OptionParser
import datetime
import os

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="write to file [FILE]", default="Test_Documentation.xls", metavar="FILE")
(options, args) = parser.parse_args()

font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True
font0.height = 240

style0 = xlwt.XFStyle()
style0.font = font0

style1 = xlwt.XFStyle()
style1.num_format_str = 'D-MMM-YY'

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

file = 'test_login.py'

def extract(file):
    '''Extracts all the docstrings from file'''
    import ast
    data = ''
    with open(file, 'r') as f:
        data = ast.parse(f.read()).body
        #  Collect the classes
        data = [i for i in data if type(i)==ast.ClassDef]
        #  Collect the functions
        fs = [i.body for i in data]
        #  Flatten
        fs = [func for funcs in fs for func in funcs]
        #  Clean
        fs = [(i.name+'\n'+ast.get_docstring(i)+'\n') for i in fs]
        fs = [i.replace('    ',' ') for i in fs]
        rmlist = ['Description:  ', 'Expected Behavior:  ', 'Test Procedure:  ']
        for i in rmlist:
            for j in fs:
                fs[fs.index(j)] = j.replace(i,'')
        return fs

def findTests(dir=os.path.dirname(os.path.realpath(__file__))):
    '''Find tests recursively starting in directory (default current directory)'''
    import os
    paths = []
    for root, dirs, files, in os.walk(dir):
        for i in files:
            if('.py' and 'test_') in i:
                if(not('.pyc') in i):
                    paths.append((root+'/'+i))
    return paths

tests = findTests()

titles = ['Test Title','Description','Expected Behavior','Test Procedure']

print(tests)

#initial row
irow = 0
for i in range(irow, len(titles)):
    ws.write(irow, i, titles[i], style0)
for file in tests:
    irow = irow+1
    ws.write(irow,0,"",style1)
    irow = irow+1
    ws.write(irow,0, file, style1)
    for docstring in extract(file):
        irow = irow+1
        for col in range(0, len(titles)):
            try:
                ws.write(irow,col,docstring.split('::')[col])
            except:
                print('error parsing docstring'+str(docstring))
                ws.write(irow,col,'error parsing docstring')

                #ws.write(irow, col, line.split('::'))

ws.write(irow+2,0,"Documentation generated on "+str(datetime.datetime.now()))
wb.save(os.path.dirname(os.path.realpath(__file__))+'/'+options.filename)
