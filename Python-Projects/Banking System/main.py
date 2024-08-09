def show_balance():
    print(f'Your Balance is ₦ {balance:.2f}')


def deposit():
    amount = float(input('Enter an amount :  '))
    if amount < 0:
        print('Invalid Deposit')
        return 0
    else:
        print(f'Your Have deposited ₦{amount} into your account')
        return amount


def withdraw():
    amount = float(input('Enter amount to be withdrawn:  '))

    if amount > balance:
        print('Insufficient Funds')
        return 0
    elif amount < 0:
        print('Invalid Number')
        return 0
    else:
        print(f'Your have withdrawn ₦{amount} from your account')
        return amount


balance = 0
is_running = True


while is_running:
    print('Banking System')
    print('1. Show Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')

    userInput = int(input('Enter your Instruction [1-4]: '))
    if userInput == 1:
        show_balance()
    elif userInput == 2:
        balance += deposit()

    elif userInput == 3:
        balance -= withdraw()
    elif userInput == 4:
        is_running = False
    else:
        print('\nInvalid Instruction\n')

print('Thank you for banking with us.')
