import random
import urllib
import sys

word_url="http://learncodethehardway.org/words.txt"
words=[]

phrases={

"class %%%(%%%)":"Make class named %%% that is a %%%",
"class %%%(object) :\n\tdef_init_(self,***)":"class %%% has a function _init_ that takes self and *** parameters.",
"class %%%(object):\n\t def_***(self,@@@)":"Class %%% has a function *** which takes a self and @@@ arguments",
"*** =%%%()":"Set *** to instance of class %%%",
"***.***(@@@)":"Call the function *** from *** class Using self and @@@ arguments",
"***.***=***":"Set *** attribute of class *** with value ***"
}

if len(sys.argv)==2 and sys.argv[1]=="english" :
    pharse_first=True
else :
    pharse_first=False
    
for word in urllib.urlopen(word_url).readlines():
    words.append(word.strip());
    
def convert(snippets,phrase):
    class_names=[w.capitalize() for w in random.sample(words,snippet.count("%%%"))]
    #print class_names
    other_names=random.sample(words,snippet.count("***"))
    #print other_names
    results=[]
    param_names=[]
    
    for i in range(0,snippet.count("@@@")):
        param_count=random.randint(1,3)
        param_names.append(','.join(random.sample(words,param_count)))
        #print param_names
        
    for sentence in [snippet, phrase]:
        #print sentence
        result=sentence[:]
        #print result
    #result=[snippet,phrase]     
        for word in class_names:
            result=result.replace('%%%',word,1)
            #print word
            #print result+"a class names"
        for word in other_names :
            result=result.replace("***",word,1)
            #print word
            #print result+"a other names"
        for word in param_names:
            result=result.replace("@@@",word,1)
            #print word
            #print result+"a param names"

        results.append(result)
    #print results
    #print result
    return results
    
try :
    while True:
        snippets=phrases.keys()
        random.shuffle(snippets)
        for snippet in snippets:
            phrase=phrases[snippet]
            question,answer=convert(snippet,phrase)
            #answer=convert(snippet,phrase).{question}
            if pharse_first:
                question,answer=answer,question
            print question
            #raw_input("->")
            #print "Answer:%s\n\n" %(answer)
            print "%s \n" %answer
except EOFError:
    print"\n BYE!"
