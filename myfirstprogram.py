import sys

print "Welcome to my first program. This might be a little cray cray."

print "Where do you work?"
workplace = raw_input()
print "What department?"
dept = raw_input()
print "What is your hourly pay rate?"
rate = float(raw_input())
print "How many hours a week do you work? Make sure you don't lie!"
hours = float(raw_input())
weekly_pay = rate * hours

print "Ok cool!"

print "Welllll all righty then! Based on your response you work at %r in the %r department and make %r dollars every week." % (workplace, dept, weekly_pay)
