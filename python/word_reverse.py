sentence = input(" enter a sentence: ")
splitlist = sentence.split()
print (splitlist)
reverse = []

i = len(splitlist)
print (i)

while i!=0:
 i = i - 1
 print (splitlist[i])
 reverse.append(splitlist[i])

str1 = ' '.join(reverse)