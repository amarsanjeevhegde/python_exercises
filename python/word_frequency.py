wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))


# Word Count
import string
test_string = "I like to study and play"
# printing original string
print ("The original string is: " + test_string)
# using sum() + strip() + split() function
res = sum([i.strip(string.punctuation).isalpha() for i in
test_string.split()])
# no of words
print ("The number of words in string are : " + str(res))