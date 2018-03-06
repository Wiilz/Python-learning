#编写一个字典程序，让用户可以添加单词和定义，然后可以查找这些单词。
#确保当要查找的单词不存在时，用户能够知晓。

dictionary = {}
while 1:    
    print "Add or look up a word (a/l/q)?"
    choose = raw_input()
    if choose == 'a':
        dicKey = raw_input("Type the word:")
        dicValue = raw_input("Type the definition:")
        dictionary = {dicKey:dicValue}
        print "word added!"
    elif choose =='l':
        queryKey = raw_input("Type the word:")
        if queryKey in dictionary:
            print dictionary[queryKey]
        else:
            print"That word isn't in the dictionary yet."
    elif choose == 'q':
        break
