# calculate gross pay, withholding tax, net pay from hourly rate and hours worked

HOURLY_RATE = 30
HOURS = 20

gross = HOURLY_RATE * HOURS
withholding = gross * 0.15
net = gross - withholding

print(f"Gross Pay:       ${gross}")
print(f"Withholding Tax: ${withholding}")
print(f"Net Pay:         ${net}")
