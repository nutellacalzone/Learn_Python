name = 'Justin Hill'
age = 35 #not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %r." % (age, height, weight, age + height + weight)

inches = 16.0
cm = inches * 2.54

kg = weight * 0.45359237

print "Converting inches to cm is easy!"
print "He's %d centimeters" % cm
print "He's %d kilograms" % kg

