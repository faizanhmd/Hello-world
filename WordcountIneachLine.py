f = open("C:\\Users\\asus\\Desktop\\Poem.txt", "r")
f_out = open("C:\\Users\\asus\\Desktop\\Poem1.txt", "w")
for line in f:
    tokens = line.split(" ")
    f_out.write("WC :" + str(len(tokens)) +" "+ line)
f.close()
f_out.close()
