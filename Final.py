print ('Lets play Odds and Evens between you and the computer')
def main():
    import random
    computer = random.randint(1, 100)
    which = {}

    def who_is_what():
        you = input('What would you like to be, odd or even  ').strip().lower()
        if you == 'odd':
            which['odd'] = 'you'
            which['even'] = 'computer'
        elif you == 'even':
            which['even'] = 'you'
            which['odd'] = 'computer'
        else:
            print ('Oops, you wrote something else...')
            who_is_what()
    who_is_what()

    def input_prompt(prompt):
        while True:
            you = input(prompt).strip().lower()
            try:
                you = int(you)
                break
            except:
                print("Error! This is not a number. Try again.")
                continue
        return you

    def rando():
        return ('The computer chose: ', computer)
    rando()

    def odd_or_even():
        abc = input_prompt("Enter your number: ")
        # print(type(you))
        print('The computer chose: ', computer)
        if (int(abc) + int(computer)) % 2 == 0:
            print(which['even'] + ' won!')
        else:
            print(which['odd'] + ' won!')
    odd_or_even()

    def ask_cont():
        while True:
            cont = input('Would you like to continue (yes or no)?').strip().lower()
            if cont == 'Yes'.strip().lower():
                main()
            elif cont == 'No'.strip().lower():
                print ('OK, goodbye!')
                exit()
            else:
                print ('you wrote something else..')
                ask_cont()
    ask_cont()

main()