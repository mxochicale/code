# Import code module
import code

bal_a = 2324
bal_b = 0
bal_c = 409
bal_d = -2

account_balances = [bal_a, bal_b, bal_c, bal_d]

def display_bal():
    for balance in account_balances:
        print(f'balance: {balance}')
        if balance < 0:
            print(f'Account balance of {balance} is below 0; add funds now.')

        elif balance == 0:
            print(f'Account balance of {balance} is equal to 0; add funds soon')

        else:
            print(f'Account balance of {balance} is above 0.')

## Use interact() function to start the interpreter with local namespace
code.interact(local=locals())
#code.interact(banner="Start", local=locals(), exitmsg="End")
#code.interact(banner="In [for-loop] how-to-construct-for-loops-in-python-3", local=locals(), exitmsg="Out of for-loop")

display_bal()
