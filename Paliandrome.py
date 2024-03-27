def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  if s==str:
    print("palindrome")
  else:
    print("not Plindrome")

s=input("Enter the string:")
reverse(s.upper())


