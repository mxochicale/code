# The parameter weekday is True if it is weekday,
# and the parameter vacation is True if we are on vacation.
# we sleepin if it is not weekend or we are on vacation.
# Return Ture if we sleep in

def sleep_in(weekday, vacation):
	if( weekday==False and vacation==True ):
		return True
	else:
		return False

def sleep_in_sol(weekend, vacation):
	return(not weekend or vacation)


weekend=False; vacation=True
#weekend=False; vacation=False
#weekend=True; vacation=False
#weekend=True; vacation=True
si=sleep_in(weekend, vacation)
print(si)


sis=sleep_in_sol(weekend, vacation)
print(sis)
