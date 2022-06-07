sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
c = 0
for x in range(0,len(sentence)):
    if sentence[x:x+5].lower() == "whale":
        c = c+1
print("There are "+str(c)+" whales in the sentence")