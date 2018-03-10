# keyboard layout
kb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
      "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
      "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "\\",
      "z", "x", "c", "v", "b", "n", "m", ",", ".", "/"]

x = []
ypsilani = []


inp1 = int(raw_input("Insert 1 to encrypt\nInsert 2 to decrypt\n>"))
print ""
inp2 = raw_input("Insert message\n>")
print ""
print "Initializing labantool..."

for i in inp2:
    a = kb.index(i)
    x.append(a)
for i in x:
    if inp1 == 1:
        ypsilani.append(kb[i - 1])
    elif inp1 == 2:
        ypsilani.append(kb[i + 1])

print "=" * (11 + len(ypsilani))
print "Message is " + ''.join(ypsilani)
print "=" * (11 + len(ypsilani))
