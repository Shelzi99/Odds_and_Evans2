def main():
    import random
    Computer = random.randint(1, 100)
    which = {}
    print ('Lets play Odds and Evens between you and the computer')
    def whoiswhat():
        You = input('What would you like to be, odd or even  ').strip().lower()
        if You == 'odd':
            which['odd'] = 'You'
            which['even'] = 'Computer'
        elif You == 'even':
            which['even'] = 'You'
            which['odd'] = 'Computer'
        else:
            print ('Oops, you wrote something else...')
            whoiswhat()
    whoiswhat()

    def t1(prompt):
        while True:
            You = input(prompt).strip().lower()
            try:
                You = int(You)
                break
            except:
                print("Error! This is not a number. Try again.")
                continue
        return You
    def rando():
        return  ('The computer chose: ',Computer)
    rando()

    def oddOReven():
        abc = t1("Enter your number: ")
        #print(type(You))
        print('The computer chose: ', Computer)
        if (int(abc) + int(Computer)) % 2 == 0:
            print (which['even'] + ' won!' )
        else:
            print (which['odd'] + ' won!')
    oddOReven()

    def askcont():
        while True:
            cont = input('Would you like to continue (yes or no)?').strip().lower()
            if 'y' in cont:
                main()
            elif 'n' in cont:
                print ('OK, goodbye!')
                exit()
            else:
                print ('You wrote something else..')
                askcont()
    askcont()

main()