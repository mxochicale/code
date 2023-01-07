# Debugging in python

## Scripts

```
conda activate simpleVE
python balances.py 
```

Logs
```
Python 3.10.8 (main, Nov 24 2022, 14:13:03) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
>>> print(account_balance)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'account_balance' is not defined
>>> print(account_balances)
[2324, 0, 409, -2]
>>> print(balance_a)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'balance_a' is not defined
>>> print(bal_a)
2324
>>> print(display_bal())
balance: 2324
Account balance of 2324 is above 0.
balance: 0
Account balance of 0 is equal to 0; add funds soon.
balance: 409
Account balance of 409 is above 0.
balance: -2
Account balance of -2 is below 0; add funds now.
None
>>> quit()
```


## References
https://www.digitalocean.com/community/tutorials/how-to-debug-python-with-an-interactive-console   
https://docs.python.org/3/library/code.html 
