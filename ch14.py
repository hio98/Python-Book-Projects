from sys import argv 

script, user_name = argv
prompt = '>'

print ("Hi %s, I am the %s script."%(user_name,script)) 
print ("I would like to ask you a few questions.")
print ("Do you like me %r?"%(user_name))
likes = input(prompt)
print ("Where do you live, %s?"%(user_name)) 
lives = input(prompt)
print ("""So you said %r about liking me and you live in %r"""%(likes,lives))