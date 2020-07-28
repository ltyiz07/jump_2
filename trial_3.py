data = "apple,4,ba,6,d,8,a,8,ba,4,c,7,g,9,h,1,a,6,ba,3,h,5,k,10,ba,3"

#words = "apple,ba,d,a,c,g,h,e"


index = 0
word = ""
word_in = ""

count = 0

for i in data:
    word = word + i
    print(word_in)
    if i == ',':
        if index % 2 == 0:
            if word_in.find("," + word + ",") < 0:
                word_in = word_in + word
        index = index + 1
        word = ""
    count = count + 1        
#i need help