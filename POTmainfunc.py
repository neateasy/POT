from docx import Document
import string


class docnode:
    Level = 0
    Num = 1


class doctree:
    CurrLevel = 0
    docnodes = []

    # 判断一个字符串的标题级别。
    def JudgeParLevel(self, str):
        if len(str) > 300:  # 太长的字符串不可能是标题，丢弃
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

    # 找出同级别编号中的最大编号
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
        print("error.message=：" + e)
        return 1
#AutoDocxNumber('1.docx','2.docx')

