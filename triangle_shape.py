
def bentuk_6(jumlah_bintang):

    if (jumlah_bintang % 2) == 1:
        for i in range(jumlah_bintang, 0 , -1):
            if (i % 2) == 1:
                bintang = ''
                space = (jumlah_bintang - i) / 2
                if (space > 0):
                    for j in range(space):
                        bintang += ' '

                bintang += '*' * i

                print(bintang + '\n')

def bentuk_5(jumlah_bintang):

    if (jumlah_bintang % 2) == 1:
        for i in range(1,(jumlah_bintang+1)):
            if (i % 2) == 1:
                bintang = ''
                space = (jumlah_bintang-i) / 2
                if(space > 0):
                    for j in range(space):
                        bintang+= ' '

                bintang += '*' * i

                print(bintang+'\n')



    else:
        print('[-] Pastikan jumlah bintang berjumlah ganjil. agar segiga sama kaki terbentuk.');
        exit()

def bentuk_4(jumlah_bintang):
    for i in range(jumlah_bintang):
        bintang = ''
        for j in range(i):
            bintang += ' '

        bintang += '*' * (jumlah_bintang-i)

        print(bintang+'\n')

def bentuk_3(jumlah_bintang):
    for i in range(jumlah_bintang):
        bintang = ''
        for j in range(jumlah_bintang-(i+1)):
            bintang += ' '

        bintang += '*' * (i+1)

        print(bintang+'\n')

def bentuk_2(jumlah_bintang):
    for i in range(jumlah_bintang):
        bintang = ''
        for j in range(jumlah_bintang-i):
            bintang += '*'

        print(bintang+'\n')

def bentuk_1(jumlah_bintang):
    for i in range(jumlah_bintang):
        bintang = ''
        for j in range(i+1):
            bintang += '*'

        print(bintang+'\n')

def ask():

    answer = raw_input('mulai lagi  (y/n) > ')

    if answer == 'y':
        mulai()
    elif answer == 'n':
        exit()
    else:
        ask()

def mulai():
    print "\n=============== LATIHAN BENTUK TERBUAT DARI BINTANG ===============\n"
    print "1. Segitiga siku siku 1"
    print "2. Segitiga siku siku 2"
    print "3. Segitiga siku siku 3"
    print "4. Segitiga siku siku 4"
    print "5. Segitiga sama kaki 1 *(angka harus ganjil"
    print "6. Segitiga sama kaki 2 *(angka harus ganjil"
    print "0. EXIT"

    pilihan = raw_input('\n\n\npilih bentuk >')

    if pilihan == '0':
        print('\n\n\nGoodBye.')
        exit()

    elif pilihan == '1':
        jumlah_bintang = raw_input('masukan jumlah bintang >')
        bentuk_1(int(jumlah_bintang))

    elif pilihan == '2':
        jumlah_bintang = raw_input('masukan jumlah bintang >')
        bentuk_2(int(jumlah_bintang))

    elif pilihan == '3':
        jumlah_bintang = raw_input('masukan jumlah bintang >')
        bentuk_3(int(jumlah_bintang))

    elif pilihan == '4':
        jumlah_bintang = raw_input('masukan jumlah bintang >')
        bentuk_4(int(jumlah_bintang))

    elif pilihan == '5':
        jumlah_bintang = raw_input('masukan jumlah bintang >')
        bentuk_5(int(jumlah_bintang))

    elif pilihan == '6':
        jumlah_bintang = raw_input('masukan jumlah bintang >')
        bentuk_6(int(jumlah_bintang))
    else:
        print "[ERROR] tidak ada pilihan " + str(pilihan)
        exit()

    ask()

if __name__=='__main__':
    try:
        mulai()

    except KeyboardInterrupt:
        print('\n\n\nGoodBye.')


