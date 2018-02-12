input_list = []
list_length = 1
max_length_list = int(input("Ilosc kwadratow"))
while len(input_list) < max_length_list:
    item = int(input("Ilosc plemnikow w kwadracie NR " + str(list_length) + ""))
    input_list.append(item)
    list_length += 1
print("Wartosci kwadratow" + str(input_list) + "")
S = int(input("Rozcieczenie"))
Ml = int(input("Ilosc Ml"))
print('%.2E' % (((((sum(input_list)/max_length_list*S)*250)/max_length_list)*1000)*Ml))
