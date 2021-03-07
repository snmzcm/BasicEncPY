def main():
    while True:
        def CaesarDecode(txt,n):
            n = int(n);
            print('OUTPUT:')
            for char in txt:
                x = ord(char) - n
                print(chr(x), end = '')
            print('\n')
        
        def CaesarCipher(txt,n):
            n = int(n);
            print('OUTPUT:')
            for char in txt:
                x = ord(char) + n
                print(chr(x), end = '')
            print('\n')


        mode = int(input('\nWhat would you like to do?\n1. Encrypt\n2. Decrypt\n'))
        if mode == 1:
            text = input('\nWrite something to encrypt\n')
            shiftValue = int(input('Enter shift value (Enter 13 for ROT13)\n'))
            CaesarCipher(text,shiftValue)
        if mode == 2:
            text = input('\nWrite something to decrypt\n')
            shiftValue = int(input('Enter shift value (Enter 13 for ROT13)\n'))
            CaesarDecode(text,shiftValue)
        
                

main()
