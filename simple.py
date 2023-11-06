Apricot = 300
Dates = 400
Almond = 500
Total1 = Apricot + Dates
Total2 = Apricot + Almond
Total3 = Dates + Almond
Total4 = Apricot + Dates + Almond
Combo1 = Total1 - (10/100 * Total1)
Combo3 = Total2 - (10/100 * Total2)
Combo2 = Total3 - (10/100 * Total3)
GiftBox = Total4 - (25/100 * Total4)
print('-' * 50)
print('''Spencer Retail
136, Garia Station Road,
Kolkata:700084''')
print('-' * 50)
print('''Product(s)      Price (per pack)
Apricot       300      
Dates         400
Almond        500''')
print(f'''Combo_1       {Combo1}
Combo_2       {Combo2}
Combo_3       {Combo3}
GiftBox       {GiftBox}
''')
print('*' * 50)
print('For free delivery, contact 123-456-789')
print('*' * 50)