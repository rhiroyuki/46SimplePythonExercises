import testModule
import string

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

def caeser_rot13(inputStr):
    outStr = ''.join([key[char] if char in string.ascii_letters else char for char in inputStr])
    return outStr

if __name__ == '__main__':
    test = testModule.UnitTester()
    test.do_test(caeser_rot13, 'a', 'n')
    test.do_test(caeser_rot13, 'a ', 'n ')
    test.do_test(caeser_rot13,'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!', 'Caesar cipher? I much prefer Caesar salad!')
    test.do_test(caeser_rot13,'!!!!!!!!!!!!!!!!!!', '!!!!!!!!!!!!!!!!!!')
    test.do_test(caeser_rot13,'', '')
    test.do_test(caeser_rot13,'1234567890', '1234567890')
    test.do_test(caeser_rot13,'abcde', 'nopqr')
