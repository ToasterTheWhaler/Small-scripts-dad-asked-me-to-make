inputlist = []
listlength = 1
maxLengthList = int(input("Ilosc kwadratow"))
while len(inputlist) < maxLengthList:
    item = int(input("Ilosc plemnikow w kwadracie NR " + str(listlength) + ""))
    inputlist.append(item)
    listlength += 1
print("Wartosci kwadratow" + str(inputlist) + "")
S = int(input("Rozcieczenie"))
Ml = int(input("Ilosc Ml"))
print('%.2E' % (((((sum(inputlist)/maxLengthList*S)*250)/maxLengthList)*1000)*Ml))
