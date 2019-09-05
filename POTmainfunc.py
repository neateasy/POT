from docx import Document
import string
import sys
import os
import time

class docnode:
    Level = 0
    Num = 1


class doctree:
    CurrLevel = 0
    docnodes = []

    #Get paragraph's Level
    def JudgeParLevel(self, str):
        if len(str) > 300:  #too long paragraph is not title.giveup it
            return 0
        a = str.split()
        if (len(a) < 2):
            return 0
        if (a[0] != 'Heading'):
            return 0
        i = int(a[1])
        if (i <= 0):
            return 0
        else:
            return i

    # get title's code
    def getLevelCode(self, nodeL):
        i = 0
        str = ''
        for kk in range(0, len(self.docnodes)):
            i = self.docnodes[kk].Num
            l = self.docnodes[kk].Level
            if (l < nodeL):
                if (l > 1):
                    str = str + '.' + '%d' % (i - 1)
                else:
                    str = '%d' % (i - 1)
                continue
            if (l == nodeL):
                if (l > 1):
                    str = str + '.' + '%d' % i
                else:
                    str = '%d' % i
                self.docnodes[kk].Num = i + 1
                continue
            if (l > nodeL):
                self.docnodes[kk].Num = 1
                continue
        return str


def AutoDocxNumber(strFin, strFout):


    try:
        dt = doctree()
        for kk in range(1, 6):
            dn = docnode()
            dn.Level = kk
            dn.Num = 1
            dt.docnodes.append(dn)

        Doc = Document(strFin)
        str = ''
        for p in (Doc.paragraphs):
            t = p.text
            i = dt.JudgeParLevel(p.style.name)
            if (i > 0):
                str = dt.getLevelCode(i)
                p.text = str + t.strip()

        Doc.save(strFout)
        return 0
    except Exception as e:
        print('error.message=:'+ e)
        return 1
#AutoDocxNumber('1.docx','2.docx')
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please input filename')
        exit(1)
    sfile = sys.argv[1]
    if not (os.path.exists(sfile)):
        print('File is not Exist')
        exit(2)
    if len(sys.argv) < 3:
        spath = os.path.dirname(sfile)
        sout = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))+'.docx'
        sout = os.path.join(spath, sout)
    else:
        sout = os.path.abspath(sys.argv[2])
        if not (os.path.exists(os.path.dirname(sout))):
            print(sout)
            print('Output file path noe exists!')
            exit(3)
    i = AutoDocxNumber(sfile, sout)
    if (i != 0):
        print('Operate file fail')
    else:
        print('Operate file success')
    exit(0)

