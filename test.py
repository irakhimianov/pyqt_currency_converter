from forex_python.converter import CurrencyRates

val = ['USD', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'RON', 'SEK', 'CHF', 'ISK', 'TRY', 'AUD', 'BRL', 'CAD', 'HKD', 'INR', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']
# val = [['USD', 'BGN'],
#        ['CZK', 'DKK'],
#        ]
print("[")
for i in range(0, len(val) - 1, 4):
    print(f"['{val[i]}', '{val[i + 1]}', '{val[i + 2]}', '{val[i + 3]}'],")
print("]")
