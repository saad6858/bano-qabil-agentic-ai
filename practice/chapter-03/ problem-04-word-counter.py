sen=input("Enter a sentence: ")
print("Total characters",len(sen))
spaces=sen.count(" ")
print("Total characters without spaces:",(len(sen))-spaces)
words=spaces+1
print("Total words:",words)