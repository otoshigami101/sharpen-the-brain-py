def largest(numbers):
    comparison = numbers
    result = [None] * len(numbers)
    for num in numbers:
        small_number = 0
        for compare in comparison:
            if int(num) > int(compare):
                small_number+=1

        index = (len(numbers) - 1) - small_number
        if result[index] == num:
            for r in result:
                if r == num:
                    index -= 1

        result[index] = num

    print "[+] RESULT : " + ' '.join(result)

def smallest(numbers):
    comparison = numbers
    result = [None] * len(numbers)
    for num in numbers:
        large_number = 0
        for compare in comparison:
            if int(num) < int(compare):
                large_number+=1

        index = (len(numbers)-1)-large_number
        if result[index] == num:
            for r in result:
                if r == num:
                    index -= 1

        result[index] = num

    print "[+] RESULT : "+' '.join(result)

def process(numbers):
    numbers = numbers.split(',')

    print "1. From smallest"
    print "2. From largest"
    orderBy = raw_input(">")

    if orderBy == "1":
        smallest(numbers)
    elif orderBy == "2":
        largest(numbers)
    else:
        process()

    ask()

def ask():
    choice = raw_input('sorting again ? (y/n) > ')
    if choice == 'y':
        start()
    elif choice == 'n':
        print "Goodbye."
    else:
        ask()

def start():
    numbers = raw_input('input number (ex : 1,2,3,4,5,...) >')
    if (str.isdigit(numbers.replace(',',''))):
        process(numbers)
    else:
        print "[-] only accepts numbers."
        start()

'''
    sorting number by otoshigami
'''
if __name__== '__main__':
    try:
        print "=============== SORTING NUMBER ==============="
        start()

    except Exception as e:
        print "[-] ERROR : "+str(e)
        print "exiting ..."
        exit()
