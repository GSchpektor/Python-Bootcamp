# Exercise 1

# def get_full_name(first_name, middle_name="", last_name=""):
# 	print(first_name,middle_name,last_name)


# Exercise 2

# def box_printer(sentence):
# 	new_sentence = sentence.split(" ")
# 	longest_word = max(new_sentence, key=len)
# 	print("*"*(len(longest_word)+5))
# 	for word in new_sentence:
# 		difference = len(longest_word) - len(word)
# 		print(f"* {word}", " "*difference, "*")
# 	print("*"*(len(longest_word)+4))

# Exercie 3

# def insertion_sort(alist):
#    for index in range(1,len(alist)):

#      currentvalue = alist[index] ## current value is the first item in list +1
#      position = index  ## number in range, 1 +1 (one ahead of currentvalue)

#      while position>0 and alist[position-1]>currentvalue: # compares the value with first item in list to see if bigger
#          alist[position]=alist[position-1] #move item down a position in the list
#          position = position-1 #keep repositioning until it is at the front

#      alist[position]=currentvalue 

# alist = [54,26,93,17,77,31,44,55,20]
# insertion_sort(alist)
# print(alist)

# Exercise 4

