print("we are going to see if your a vampire.")
print('Please give us your age.')
myage = int(input())
if myage <= 10:
    print("we're not sure if you a vampire yet so cross your fingers")
elif myage <= 100:
    print('Probly just an old man but i have one more question')
elif myage > 2000:
    print('You could be an immortal vampire but you could also be a witch')
else:
    print('we could not determine your age definately lieing')
print('Are you allergic to the sun?')
myanswer = str(input())
if myanswer == "yes":
    print("you are a most likely a vampire or just one really unlucky person.")
elif myanswer == "no":
    print("you might still be a witch but not a vampire.")
else:
    print("you are definately a vampire")
