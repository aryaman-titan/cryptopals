#This is a solution to Set-1->Challenge-4

file = open("4.txt" , 'r')
data = file.read()
file.close()
decoded = data.decode("hex")
print (decoded)