fw = open("res/lines.txt", "w")

list_to_write = [x for x in range(51) if x % 2 == 0]

for number in list_to_write:
    fw.write(str(number) + '\n')

fw.close()

fr = open("res/lines.txt", "r")

for line in fr:
    print line,

fr.close()