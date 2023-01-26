import re 

numbers = [
    "555.123.4565", 
    "+1-(800)-545-2468", 
    "2-(800)-545-2468", 
    "3-800-545-2468", 
    "555-123-3456", 
    "555 222 3342", 
    "(234) 234 2442", 
    "(243)-234-2342", 
    "1234567890", 
    "123.456.7890", 
    "123.4567", 
    "123-4567", 
    "1234567900", 
    "12345678900"
    ]
checked = []
countYes= 0
for _n in numbers:
    join_match = re.findall('[0-9()+-.\s]', _n)
    join = ''.join(join_match)
    match = "No" 
    if(_n == join):
        match = "Yes"
        countYes+=1
    checked.append({
        'Number':_n,
        'Matched':match,
    })
print("Check Numbers",checked)

if len(numbers) == countYes:
    print(f'All {countYes} checked')
  






    


