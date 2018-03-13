# can hard-code it into saying letters 1,q,a,z,=,],\,\,/ all have different outputs
# keyboard layout
kb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
      "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]",
      "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "\\",
      "z", "x", "c", "v", "b", "n", "m", ",", ".", "/"]

x = []
ypsilani = []
exceptional = ["1", "=", "q", "]", "a", "\\", "z", "/"]
count = 0
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
        for k in exceptional:
            if kb[i] == k:
                ypsilani.append(k)
                count += 1
        if count == 0:
            ypsilani.append(kb[i - 1])
        count = 0
    elif inp1 == 2:
        for k in exceptional:
            if kb[i] == k:
                ypsilani.append(k)
                count += 1
        if count == 0:
            ypsilani.append(kb[i + 1])
        count = 0
print "=" * (11 + len(ypsilani))
print "Message is " + ''.join(ypsilani)
print "=" * (11 + len(ypsilani))
