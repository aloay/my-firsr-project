#input
from gtts import gTTS

name=input("enter your name :")
arabic=eval(input('enter your degree in ar :'))
english=eval(input('enter your degree in en :'))
frensh=eval(input('enter your degree in fr :'))
math=eval(input('enter your degree in ma :'))

#process                                                                                                    برنامج حساب مجموع ومتوسط الطالب 

total=arabic+english+frensh+math
average=total/4

#output

print("name is :",name, "total is :",total, "average is :",average,)

print("(good luck guys )")

