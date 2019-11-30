def count():
    Line = 0
    sentence = 0
    word = 0
    strs = 0
    strupper = 0
    strlower = 0
    strssp = 0
    read = open('Loop.txt','r')
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in read:
       Line += 1
       i = i.split(".")
       for o in i[:-1]:
            sentence += 1
            o = o.split()
            for p in o:
                word += 1
                for u in p:
                    if u in abc:
                        strlower += 1
                    elif u in ABC:
                        strupper += 1
                    else:
                        strssp += 1
                    strs += 1
    read.close()
    Dsiplay(strssp,strlower,strupper,strs,word,sentence,Line) 
def Dsiplay(strssp,strlower,strupper,strs,word,sentence,Line):
    print("1.Line :",Line)
    print("2.Sentence :",sentence)
    print("3.Words :",word)
    print("4.Character :",strs) #ไม่นับจุด
    print("5.Character upper:",strupper) 
    print("6.Character lower:",strlower)
    print("7.Special Character:",strssp) #ไม่นัดจุด
def main():
    count()
main()