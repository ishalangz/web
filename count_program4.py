t=str(input("enter a sentence:"))
a=t.split()
w_count={}
for word in a:
    if word in w_count:
        w_count[word]+=1
    else:
         w_count[word]=1
print(w_count)
