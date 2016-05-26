from sys import argv

script, user_name = argv
youtype = 'write your answer here:'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few question."
print "Do you like me %s?" % user_name
likes = raw_input(youtype)

print "Where do you live %s?" % user_name
lives = raw_input(youtype)

print "What kind of computer do you have?"
computer = raw_input(youtype)

print "What kind of phone do you use?"
phone = raw_input(youtype)

print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is.
You have a %r computer and a %r phone. Nice.
""" %  (likes, lives, computer, phone)


