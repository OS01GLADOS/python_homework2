"""

1. Реализуйте функцию постановки слова «рубль» в подходящее число и падеж
в зависимости от введенного целого числа
(ввели «0» – функция возвращает «рублей», ввели «1» – «рубль», ввели «2» – «рубля» и т. д.).(done)
2. Реализуйте функцию постановки слова «копейка»
в подходящее число и падеж в зависимости от введенного целого числа
(ввели «0» – функция возвращает «копеек», ввели «1» – «копейка», ввели «2» – «копейки» и т. д.).(done)
3. Реализуйте функцию вывода введенного числа прописью в мужском роде
(ввели «0» – функция возвращает «ноль», ввели «1» – «один», ввели «2» – «два» и т. д. до «999»).
4. Реализуйте функцию вывода введенного числа прописью в женском роде (ввели «0» – функция возвращает «ноль», ввели «1» – «одна», ввели «2» – «две» и т. д. до «999»).
5. Используя предыдущие функции, реализуйте еще одну функцию, которая будет выводить введенную сумму денег с плавающей точкой прописью (ввели «0,70» – функция возвращает «ноль рублей семьдесят копеек»).
"""
import math

def moneyRuble(amount):
    if amount>=10:
        amount1 = amount
        amount = amount % 10
    else: amount1 = amount
    if(amount == 0) or (amount > 4) or (amount1 in range(11,15)):
        return ' рублей '
    elif (amount ==1):
        return ' рубль '
    else:
        return ' рубля '

def moneyCent(amount):
    if amount>=10:
        amount1 = amount
        amount = amount % 10
    else: amount1 = amount
    if(amount == 0) or (amount > 4) or (amount1 in range(11,15)):
        return ' копеек '
    elif amount ==1:
        return  ' копейка '
    else:
        return ' копейки'

def malePropis(amount):
    #
    #десят
    ed = amount %10
    des = int(amount % 100 - ed)//10
    sot = amount //100

    numbers = ['один', 'два', 'три','четыре','пять','шесть','семь','восемь','девять']

    printEd = ''
    printSot = ''
    printDes = ''

    if amount ==0:
        printEd = 'ноль'
    elif amount <10:
        printEd =(numbers[ed-1])
    elif amount == 10:
        printDes ='десять'
    elif amount in range (11,20,1):
        if (ed ==2):
            printDes =  numbers[ed - 1][:-1] + 'енадцать'
        elif (ed ==4 or ed == 6 or ed == 9):
            printDes =  numbers[ed-1][:-1]+'надцать'
        else:
            printDes = numbers[ed-1]+'надцать'
    elif amount in range (20,100,1):
        if des in range (2,4,1):
            printDes = numbers[des-1]+'дцать '
        elif des == 4:
            printDes = 'Сорок '
        elif des in range (5,9,1):
            printDes = numbers[des-1]+'десят '
        else:
            printDes = 'Девяносто '

        if ed != 0:
            printEd  = numbers[ed-1]

    elif amount in range(100,1000,1):

            if sot == 1:
                printSot = 'сто '
            elif sot == 2:
                printSot = 'двесте '
            elif sot in range(2,4,1):
                printSot = numbers[sot-1]+'ста '
            elif sot in range (5,10,1):
                printSot = numbers[sot - 1] + 'сот '




            if des*10+ed == 10:
                 printDes = 'десять'
            elif des*10+ed in range(11, 20, 1):
                if (ed == 2):
                    printDes =  numbers[ed - 1][:-1] + 'енадцать'
                elif (ed == 4 or ed == 6 or ed == 9):
                    printDes = numbers[ed - 1][:-1] + 'надцать'
                else:
                    return printSot+numbers[ed - 1] + 'надцать'
            elif des*10 in range(20, 100, 1):
                if des in range(2, 4, 1):
                    printDes = numbers[des - 1] + 'дцать '
                elif des == 4:
                    printDes = 'сорок '
                elif des in range(5, 9, 1):
                    printDes = numbers[des - 1] + 'десят '
                else:
                    printDes = 'девяносто '
            if ed != 0:
                printEd = numbers[ed - 1]

    return printSot+printDes+printEd


def femalePropis(amount):
    #
    #десят
    ed = amount %10
    des = int(amount % 100 - ed)//10
    sot = amount //100

    numbers = ['один', 'две', 'три','четыре','пять','шесть','семь','восемь','девять']

    printEd = ''
    printSot = ''
    printDes = ''

    if amount ==0:
        printEd = 'ноль'
    elif amount <10:
        if ed == 1:
            printEd = 'одна'
        else:printEd =(numbers[ed-1])
    elif amount == 10:
        printDes ='десять'
    elif amount in range (11,20,1):
        if (ed ==2):
            printDes =  numbers[ed - 1][:-1] + 'енадцать'
        elif (ed ==4 or ed == 6 or ed == 9):
            printDes =  numbers[ed-1][:-1]+'надцать'
        else:
            printDes = numbers[ed-1]+'надцать'
    elif amount in range (20,100,1):
        if des in range (2,4,1):
            if des ==2:
                printDes ='двадцать '
            else:
                printDes = numbers[des-1]+'дцать '
        elif des == 4:
            printDes = 'Сорок '
        elif des in range (5,9,1):
            printDes = numbers[des-1]+'десят '
        else:
            printDes = 'Девяносто '

        if ed == 1:
            printEd = 'одна'
        elif ed == 0:
            printEd  ==''

        else:printEd =(numbers[ed-1])

    elif amount in range(100,1000,1):

            if sot == 1:
                printSot = 'сто '
            elif sot == 2:
                printSot = 'двесте '
            elif sot in range(2,4,1):
                printSot = numbers[sot-1]+'ста '
            elif sot in range (5,10,1):
                printSot = numbers[sot - 1] + 'сот '

            if des*10+ed == 10:
                 printDes = 'десять'
            elif des*10+ed in range(11, 20, 1):
                if (ed == 2):
                    printDes =  numbers[ed - 1][:-1] + 'енадцать'
                elif (ed == 4 or ed == 6 or ed == 9):
                    printDes = numbers[ed - 1][:-1] + 'надцать'
                else:
                    return printSot+numbers[ed - 1] + 'надцать'
            elif des*10 in range(20, 100, 1):
                if des in range(2, 4, 1):
                    printDes = numbers[des - 1] + 'дцать '
                elif des == 4:
                    printDes = 'сорок '
                elif des in range(5, 9, 1):
                    printDes = numbers[des - 1] + 'десят '
                else:
                    printDes = 'девяносто '
            if ed == 1:
                printEd = 'одна'
            elif ed == 0:
                printEd == ''

            else:
                printEd = (numbers[ed - 1])

    return printSot+printDes+printEd

def moneyout(amount):
    rub = int(math.trunc(amount))
    kop = int((amount-rub)*100)

    res = malePropis(rub)+moneyRuble(rub)+femalePropis(kop)+moneyCent(kop)
    return res

print(moneyout(123.67))