palindrome = "civic"
p_list = list(palindrome)
p_re_list = list(palindrome)
p_re_list.reverse()
print (palindrome)
print (p_list)
print (p_re_list)
if p_list == p_re_list:
    print ("palindrome")
else:
    print ("not palindrome")