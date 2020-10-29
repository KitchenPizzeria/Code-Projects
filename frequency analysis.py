import csv

text ="SADTSTDAHNPGLFSMTDNPBDOSCNCBDPISCHHFGNVFGNHMDPALTDHPMMGXNSCALXSCMLOSCNVDPBHSGHHFPHVPNVFPHHFDXSCAHOXSBSADBPNRDLTDPHHFDGAUCGBOGHGNTONHBSAEGTJBDNNGSAHFPHGFDPBLGHPALODHPTSAEHFDXBPNFSQHFDEPMDPALHFDXBDPRGAESQPASMLFSCNDGTPOJSNNGIMOFPWDIDDALDXDGWDLVPNOSCBNGNHDBLBDNNDLASNFDVPNGAFDBAGEFHLBDNNGAFDBBGEFHFPALVPNQSCALHFDXFPBBDLNHCTJSQPTPHXFPALGAFDBMDQHPTPHXFISYNFSVGAEHFPHNFDFPLNHBCXRPMGEFHPALMSSRDLPISCHFDBVFDAHFDPMPBTHSSRJMPXDHFPHGNGTJSBHPAHPALVFPHXSAXMCNGSANLGLHFDXSBSADBXSTDHSFDGAWDNHGEPHDLHFDXPNDVGHFEBDPHXPBDQSBLBBSOMSHHNXSALCXHFPLMSAEIDDAASHSBGSCNGAHFDXSCAHOICHFDVPNCAPIMDHSQGALPAONPHGNQPXHSBOXPCNDSQLDPHFTODWGLDAXDNFSVDLHFPHHFDLSSBFPLIDDAQPNHDADLCJSAHFDGAADBNGLDPALHFDVGALSVNVDBDIMSXRDLIOSMLQPNFGSADLNFCHHDBNVGHFIBSPLGBSAIPBNVFGXFVDBDNDXCBDLDWDBOAGEFHHFDVPMMNVDBDXPBDQCMMONSCALDLPALVDBDNFSVAHSIDUCGHDNSMGLPMMBSCALPALHFDQMSSBGAEVPNPMNSHFSBSCEFMODYPTGADLVGHFHFDNPTDBDNCMHHFDXFGTADOGNVGLDICHGNIPBBDLCJIOQSCBMPBEDNHPJMDNGHGNXDBHPGAHFDBDQSBDHFPHTONGNHDBVPNUCGHDPMSADVFDANFDTDHFDBDALIDNGLDNHFDBDVDBDASTPBRNSQPAOWGSMDAXDCJSAFDB"

def getKey(item):
    return item[1]

def ChiSquared(Text):
    ObservedFreq = FreqAnal(Text)
    ChiStat = 0
    with open('ChiSquared.csv') as ChiSquared:
        ExpectedFreq = csv.reader(ChiSquared)
        for EachRow in ExpectedFreq:
            for x in range(len(ObservedFreq)):
                if EachRow[0] == ObservedFreq[x][0]:
                    print(ObservedFreq[x][0],EachRow[1],ObservedFreq[x][1]/float(len(Text)))

def UpdateList(Pairs):
    Before = str(input("Cipher Letter: "))
    After = str(input("Corresponding Key: "))
    with open("Key.csv","r") as KeyFile:
        reader = csv.reader(KeyFile)
        for x in reader:
            if x[0] == Before.upper():
                writer = csv.writer(KeyFile)
                writer.writerow([str(x[0]),str(After)])
    KeyFile.close()
            
    #HowMany = int(input("\nHow many updates: "))
    #for x in range(HowMany):
    #    Before = str(input("Cipher Letter: "))
    #    After = str(input("Corresponding Key: "))
    #    Pairs[ord(Before.upper())-65] = After.lower()

    #for x in range(26):
    #    print(chr(x+65)+" --> "+Pairs[x])

    return Pairs
    
def Decrypt(Text,Pairs):
    for x in range(len(Text)):
        place = ord(Text[x])-65
        Text[x] = Pairs[place]
    print()
    print("".join(Text))
    print()
    

def PopulateList(n,Text):
    Letters = []
    if n == 1:
        for x in range(65,91):
            Letters.append([chr(x),0])
    if n == 2:
        for x in range(len(Text)-2):
            Phrase = str(Text[x])+str(Text[x+1])+str(Text[x+2])
            Letters.append(Phrase)
    if n == 3:
        for x in range(len(Text)-2):
            if Text[x] == Text[x+1]:
                Double = str(Text[x])+str(Text[x+1])
                Letters.append(Double)
    return Letters

def FreqAnal(Text):
    List = PopulateList(1,Text)
    for x in Text:
        for y in List:
            if x == y[0]:
                y[1]+=1

    return sorted(List, key=getKey,reverse=True)

def Analysis(Text):
    BaseList = PopulateList(2,Text)
    count = []
    for x in BaseList:
        if BaseList.count(x)>3:
            count.append([x,BaseList.count(x)])

    Count = []
    for i in count:
        if i not in Count:
            Count.append(i)
    
    for x in sorted(Count, key=getKey,reverse = True):
        print(str(x[0])+" --> "+str(x[1]))
        

def DigramPlaces(Text):
    for x in range(len(Text)-2):
        if str(Text[x]+Text[x+1])=="HF":
            print(x,x+1)
            
def DoubleLetterCount(Text):
    Doubles = PopulateList(3,Text)
    count = []      
    for x in Doubles:
        count.append([x,Doubles.count(x)])

    Count = []
    for i in count:
        if i not in Count:
            Count.append(i)
    
    for x in sorted(Count, key=getKey,reverse=True):
        print(str(x[0])+" --> "+str(x[1]))

def Menu(Pairs,text):
    print('''
------------------MENU--------------------

    1. View Key Table
    2. Update Key Table
    3. Display Plaintext
    4. Frequency Analysis
    5. Trigram Anaylsis
    6. Double Letter Analysis
    7. Digram Distances
    8. Chi-Squared

------------------------------------------''')
    Choice = 0
    try:
        Choice = int(input("Choice: "))
    except:
        print("\n**Try Again**")
    print("------------------------------------------")

    if Choice == 1:
        with open("Key.csv","r") as KeyFile:
            reader = csv.reader(Keyfile)
            for x in reader:
                print(str(x[0])+" --> "+str(x[1]))
    elif Choice == 2:
        NewPairs = UpdateList(Pairs)
        Decrypt(list(text),NewPairs)
    elif Choice == 4:
        List = FreqAnal(list(text))
        for x in List:
            print(x[0],"-->",x[1])
    elif Choice == 6:
        DoubleLetterCount(list(text))
    elif Choice == 5:
        Analysis(list(text))
    elif Choice == 3:
        Decrypt(list(text),Pairs)
    elif Choice == 6:
        DigramPlaces(text)
    elif Choice == 8:
        ChiSquared(text)
    Menu(Pairs,text)
    
Key = ["_" for x in range(26)]
Menu(Key,text)
