import string

password = 'Lei6i@rht*9a3u'

len_pass = len(password) >= 8

upper_flag = False
lower_flag = False
special_flag = False

for char in password:
      if char.isupper():
        print(True)
for char in password:
      if char.islower():
        print(True)
for char in password:
      if char in string.punctuation:
        print(True)
