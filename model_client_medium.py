# File name: model_client_medium.py
# This file is used to test the model deployment. It sends a request to the model server and prints the response.
# The tests in this file represent a medium workload.

import requests
import time

start_time = time.time()

t1 = "I like salads."
t2 = "Hello world."
t3 = "The quick brown fox jumps over the lazy dog."
t4 = "She sells seashells by the seashore."
t5 = "The sun is shining and the birds are singing."
t6 = "The cat in the hat is wearing a red and white striped hat."
t7 = "The sky is blue and the grass is green."
t8 = '"The quick brown fox jumps over the lazy dog" is a pangram that contains all the letters of the English alphabet.'
t9 = "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"
t10 = "City of stars, are you shining just for me?"
t11 = "The early bird catches the worm."
t12 = "I scream, you scream, we all scream for ice cream!"
t13 = "The pen is mightier than the sword."
t14 = "A picture is worth a thousand words."
t15 = "When in Rome, do as the Romans do."
t16 = "An apple a day keeps the doctor away."
t17 = "You can't judge a book by its cover."
t18 = "Actions speak louder than words."
t19 = "All's fair in love and war."
t20 = "Beauty is in the eye of the beholder."
t21 = "The grass is always greener on the other side."
t22 = "The customer is always right."
t23 = "Don't judge a man until you have walked a mile in his shoes."
t24 = "Honesty is the best policy."
t25 = "If at first you don't succeed, try, try again."
t26 = "Laughter is the best medicine."
t27 = "Life is like a box of chocolates; you never know what you're going to get."
t28 = "Money can't buy happiness."
t29 = "Practice makes perfect."
t30 = "There's no place like home."
t31 = "The early bird gets the worm."
t32 = "I'm on top of the world!"
t33 = "It's raining cats and dogs outside."
t34 = "Life is too short to waste time on things that don't matter."
t35 = "Love conquers all."
t36 = "Nothing ventured, nothing gained."
t37 = "One man's trash is another man's treasure."
t38 = "The proof of the pudding is in the eating."
t39 = "There's no such thing as a free lunch."
t40 = "Time heals all wounds."
t41 = "Time heals all wounds."
t42 = "To be or not to be, that is the question."
t43 = "Two heads are better than one."
t44 = "Variety is the spice of life."
t45 = "Where there's smoke, there's fire."
t46 = "You can't have your cake and eat it too."
t47 = "You can't make an omelette without breaking eggs."
t48 = "You can't please everyone."
t49 = "You reap what you sow."
t50 = "You're never too old to learn something new."
t51 = "A watched pot never boils."
t52 = "All good things must come to an end."
t53 = "All is well that ends well."
t54 = "An ounce of prevention is worth a pound of cure."
t55 = "As you sow, so shall you reap."
t56 = "Beggars can't be choosers."
t57 = "Better late than never."
t58 = "Curiosity killed the cat."
t59 = "Every cloud has a silver lining."
t60 = "Fortune favors the bold."
t61 = "Fortune favors the bold."
t62 = "The early bird catches the worm."
t63 = "Actions speak louder than words."
t64 = "When in Rome, do as the Romans do."
t65 = "All is fair in love and war."
t66 = "The pen is mightier than the sword."
t67 = "You can't make an omelette without breaking eggs."
t68 = "The proof of the pudding is in the eating."
t69 = "A picture is worth a thousand words."
t70 = "Don't count your chickens before they're hatched."
t71 = "A watched pot never boils."
t72 = "Beggars can't be choosers."
t73 = "Curiosity killed the cat."
t74 = "Don't bite the hand that feeds you."
t75 = "Don't put all your eggs in one basket."
t76 = "Easy come, easy go."
t77 = "Every cloud has a silver lining."
t78 = "Honesty is the best policy."
t79 = "If at first you don't succeed, try, try again."
t80 = "It's no use crying over spilt milk."
t81 = "Laughter is the best medicine."
t82 = "Let sleeping dogs lie."
t83 = "Money doesn't grow on trees."
t84 = "Necessity is the mother of invention."
t85 = "No pain, no gain."
t86 = "Out of sight, out of mind."
t87 = "Practice makes perfect."
t88 = "Rome wasn't built in a day."
t89 = "The squeaky wheel gets the grease."
t90 = "There's no place like home."
t91 = "Time heals all wounds."
t92 = "When the going gets tough, the tough get going."
t93 = "Where there's smoke, there's fire."
t94 = "You can lead a horse to water but you can't make it drink."
t95 = "You can't judge a book by its cover."
t96 = "You can't have your cake and eat it too."
t97 = "You reap what you sow."
t98 = "A chain is only as strong as its weakest link"
t99=  'A journey of a thousand miles begins with a single step'
t100= 'A penny saved is a penny earned'

r1 = requests.post("http://127.0.0.1:8000/", json=t1)
print(r1.text)

r2 = requests.post("http://127.0.0.1:8000/", json=t2)
print(r2.text)

r3 = requests.post("http://127.0.0.1:8000/", json=t3)
print(r3.text)

r4 = requests.post("http://127.0.0.1:8000/", json=t4)
print(r4.text)

r5 = requests.post("http://127.0.0.1:8000/", json=t5)
print(r5.text)

r6 = requests.post("http://127.0.0.1:8000/", json=t6)
print(r6.text)

r7 = requests.post("http://127.0.0.1:8000/", json=t7)
print(r7.text)

r8 = requests.post("http://127.0.0.1:8000/", json=t8)
print(r8.text)

r9 = requests.post("http://127.0.0.1:8000/", json=t9)
print(r9.text)

r10 = requests.post("http://127.0.0.1:8000/", json=t10)
print(r10.text)

r11 = requests.post("http://127.0.0.1:8000/", json=t11)
print(r11.text)

r12 = requests.post("http://127.0.0.1:8000/", json=t12)
print(r12.text)

r13 = requests.post("http://127.0.0.1:8000/", json=t13)
print(r13.text)

r14 = requests.post("http://127.0.0.1:8000/", json=t14)
print(r14.text)

r15 = requests.post("http://127.0.0.1:8000/", json=t15)
print(r15.text)

r16 = requests.post("http://127.0.0.1:8000/", json=t16)
print(r16.text)

r17 = requests.post("http://127.0.0.1:8000/", json=t17)
print(r17.text)

r18 = requests.post("http://127.0.0.1:8000/", json=t18)
print(r18.text)

r19 = requests.post("http://127.0.0.1:8000/", json=t19)
print(r19.text)

r20 = requests.post("http://127.0.0.1:8000/", json=t20)
print(r20.text)

r21 = requests.post("http://127.0.0.1:8000/", json=t21)
print(r21.text)

r22 = requests.post("http://127.0.0.1:8000/", json=t22)
print(r22.text)

r23 = requests.post("http://127.0.0.1:8000/", json=t23)
print(r23.text)

r24 = requests.post("http://127.0.0.1:8000/", json=t24)
print(r24.text)

r25 = requests.post("http://127.0.0.1:8000/", json=t25)
print(r25.text)

r26 = requests.post("http://127.0.0.1:8000/", json=t26)
print(r26.text)

r27 = requests.post("http://127.0.0.1:8000/", json=t27)
print(r27.text)

r28 = requests.post("http://127.0.0.1:8000/", json=t28)
print(r28.text)

r29 = requests.post("http://127.0.0.1:8000/", json=t29)
print(r29.text)

r30 = requests.post("http://127.0.0.1:8000/", json=t30)
print(r30.text)

r31 = requests.post("http://127.0.0.1:8000/", json=t31)
print(r31.text)

r32 = requests.post("http://127.0.0.1:8000/", json=t32)
print(r32.text)

r33 = requests.post("http://127.0.0.1:8000/", json=t33)
print(r33.text)

r34 = requests.post("http://127.0.0.1:8000/", json=t34)
print(r34.text)

r35 = requests.post("http://127.0.0.1:8000/", json=t35)
print(r35.text)

r36 = requests.post("http://127.0.0.1:8000/", json=t36)
print(r36.text)

r37 = requests.post("http://127.0.0.1:8000/", json=t37)
print(r37.text)

r38 = requests.post("http://127.0.0.1:8000/", json=t38)
print(r38.text)

r39 = requests.post("http://127.0.0.1:8000/", json=t39)
print(r39.text)

r40 = requests.post("http://127.0.0.1:8000/", json=t40)
print(r40.text)

r41 = requests.post("http://127.0.0.1:8000/", json=t41)
print(r41.text)

r42 = requests.post("http://127.0.0.1:8000/", json=t42)
print(r42.text)

r43 = requests.post("http://127.0.0.1:8000/", json=t43)
print(r43.text)

r44 = requests.post("http://127.0.0.1:8000/", json=t44)
print(r44.text)

r45 = requests.post("http://127.0.0.1:8000/", json=t45)
print(r45.text)

r46 = requests.post("http://127.0.0.1:8000/", json=t46)
print(r46.text)

r47 = requests.post("http://127.0.0.1:8000/", json=t47)
print(r47.text)

r48 = requests.post("http://127.0.0.1:8000/", json=t48)
print(r48.text)

r49 = requests.post("http://127.0.0.1:8000/", json=t49)
print(r49.text)

r50 = requests.post("http://127.0.0.1:8000/", json=t50)
print(r50.text)

r51 = requests.post("http://127.0.0.1:8000/", json=t51)
print(r51.text)

r52 = requests.post("http://127.0.0.1:8000/", json=t52)
print(r52.text)

r53 = requests.post("http://127.0.0.1:8000/", json=t53)
print(r53.text)

r54 = requests.post("http://127.0.0.1:8000/", json=t54)
print(r54.text)

r55 = requests.post("http://127.0.0.1:8000/", json=t55)
print(r55.text)

r56 = requests.post("http://127.0.0.1:8000/", json=t56)
print(r56.text)

r57 = requests.post("http://127.0.0.1:8000/", json=t57)
print(r57.text)

r58 = requests.post("http://127.0.0.1:8000/", json=t58)
print(r58.text)

r59 = requests.post("http://127.0.0.1:8000/", json=t59)
print(r59.text)

r60 = requests.post("http://127.0.0.1:8000/", json=t60)
print(r60.text)

r61=requests.post("http://127.0.0.1:8000/", json=t61)
print(r61.text)

r62=requests.post("http://127.0.0.1:8000/", json=t62)
print(r62.text)

r63=requests.post("http://127.0.0.1:8000/", json=t63)
print(r63.text)

r64=requests.post("http://127.0.0.1:8000/", json=t64)
print(r64.text)

r65=requests.post("http://127.0.0.1:8000/", json=t65)
print(r65.text)

r66=requests.post("http://127.0.0.1:8000/", json=t66)
print(r66.text)

r67=requests.post("http://127.0.0.1:8000/", json=t67)
print(r67.text)

r68=requests.post("http://127.0.0.1:8000/", json=t68)
print(r68.text)

r69=requests.post("http://127.0.0.1:8000/", json=t69)
print(r69.text)

r70=requests.post("http://127.0.0.1:8000/", json=t70)
print(r70.text)

r71=requests.post("http://127.0.0.1:8000/", json=t71)
print(r71.text)

r72=requests.post("http://127.0.0.1:8000/", json=t72)
print(r72.text)

r73=requests.post("http://127.0.0.1:8000/", json=t73)
print(r73.text)

r74=requests.post("http://127.0.0.1:8000/", json=t74)
print(r74.text)

r75=requests.post("http://127.0.0.1:8000/", json=t75)
print(r75.text)

r76=requests.post("http://127.0.0.1:8000/", json=t76)
print(r76.text)

r77=requests.post("http://127.0.0.1:8000/", json=t77)
print(r77.text)

r78=requests.post("http://127.0.0.1:8000/", json=t78)
print(r78.text)

r79=requests.post("http://127.0.0.1:8000/", json=t79)
print(r79.text)

r80=requests.post("http://127.0.0.1:8000/", json=t80)
print(r80.text)

r81=requests.post("http://127.0.0.1:8000/", json=t81)
print(r81.text)

r82=requests.post("http://127.0.0.1:8000/", json=t82)
print(r82.text)

r83=requests.post("http://127.0.0.1:8000/", json=t83)
print(r83.text)

r84=requests.post("http://127.0.0.1:8000/", json=t84)
print(r84.text)

r85=requests.post("http://127.0.0.1:8000/", json=t85)
print(r85.text)

r86=requests.post("http://127.0.0.1:8000/", json=t86)
print(r86.text)

r87=requests.post("http://127.0.0.1:8000/", json=t87)
print(r87.text)

r88=requests.post("http://127.0.0.1:8000/", json=t88)
print(r88.text)

r89=requests.post("http://127.0.0.1:8000/", json=t89)
print(r89.text)

r90=requests.post("http://127.0.0.1:8000/", json=t90)
print(r90.text)

r91=requests.post("http://127.0.0.1:8000/", json=t91)
print(r91.text)

r92=requests.post("http://127.0.0.1:8000/", json=t92)
print(r92.text)

r93=requests.post("http://127.0.0.1:8000/", json=t93)
print(r93.text)

r94=requests.post("http://127.0.0.1:8000/", json=t94)
print(r94.text)

r95=requests.post("http://127.0.0.1:8000/", json=t95)
print(r95.text)

r96=requests.post("http://127.0.0.1:8000/", json=t96)
print(r96.text)

r91=requests.post("http://127.0.0.1:8000/", json=t91)
print(r91.text)

r97=requests.post("http://127.0.0.1:8000/", json=t97)
print(r97.text)

r98=requests.post("http://127.0.0.1:8000/", json=t98)
print(r98.text)

r99=requests.post("http://127.0.0.1:8000/", json=t99)
print(r99.text)

r100=requests.post("http://127.0.0.1:8000/", json=t100)
print(r100.text)

print("--- %s seconds ---" % (time.time() - start_time))