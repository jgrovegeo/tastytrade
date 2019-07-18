from datetime import datetime, timedelta
from tabulate import tabulate

while True:
    print('Type width or position command. Type exit to close script.\n')
    command = input('Enter command: ')

    width = ['one - .33', 'two - .66', 'three - .99', 'four - 1.32', 'five - 1.65',
            'six - 1.98', 'seven - 2.31', 'eight - 2.64', 'nine - 2.97', 'ten - 3.30']
    
    # PRINTS OUT PREMIUM REQUIRED FOR COLLECTING 1/3 WIDTH OF STRIKES
    if command == 'width':
        print('\nCollect 1/3 width of strikes')
        for i in width:
            print('\n',i)
        print('\n')
        continue

    # USER ENTERS POSITION INFORMATION AND PRINTS OUT A TABLE             
    elif command == 'position':
        date = input('\nDate filled: ')
        date_obj = datetime.strptime(date,'%Y-%m-%d').date()
        sym = input('Ticker: ')
        ivr = input('IVR: ')
        premty = input('Premium Type (credit or debit): ')
        prem = float(input('Premium: '))
        exp = input('Expiration: ')
        exp_obj = datetime.strptime(exp,'%Y-%m-%d').date()
        print('\n')
        print('Exit trade 21 days prior to expiration:', exp_obj + timedelta(days=-21))
        print('\n')
        
        if premty == 'credit':
            table = tabulate([['10%', round(prem - (prem*.10), 2), '3', date_obj + timedelta(days=3)], 
                            ['20%', round(prem - (prem*.20), 2), '6', date_obj + timedelta(days=6)],
                            ['30%', round(prem - (prem*.30), 2), '10', date_obj + timedelta(days=10)],
                            ['40%', round(prem - (prem*.40), 2), '15', date_obj + timedelta(days=15)],
                            ['50%', round(prem - (prem*.50), 2), '19', date_obj + timedelta(days=19)],
                            ['60%', round(prem - (prem*.60), 2), '24', date_obj + timedelta(days=24)]],
                            headers=['% of Max Profit', 'Premium', 'Avg. Days Held', 'Date'], 
                            tablefmt='orgtbl')
            print(table)
        
        if premty == 'debit':
            table = tabulate([['10%', round(prem + (prem*.10), 2), '3', date_obj + timedelta(days=3)], 
                            ['20%', round(prem + (prem*.20), 2), '6', date_obj + timedelta(days=6)],
                            ['30%', round(prem + (prem*.30), 2), '10', date_obj + timedelta(days=10)],
                            ['40%', round(prem + (prem*.40), 2), '15', date_obj + timedelta(days=15)],
                            ['50%', round(prem + (prem*.50), 2), '19', date_obj + timedelta(days=19)],
                            ['60%', round(prem + (prem*.60), 2), '24', date_obj + timedelta(days=24)]],
                            headers=['% of Max Profit', 'Premium', 'Avg. Days Held', 'Date'], 
                            tablefmt='orgtbl')
            print(table)            

        # WRITES DATA TO A TEXT FILE
        with open('/home/jared/Desktop/positions.txt', 'a') as f:
            f.write('\n')
            f.write('Symbol: ' + str(sym) + '\n')
            f.write('IV rank: ' + str(ivr) + '\n')
            f.write('Premium type: ' + premty + '\n')
            f.write('Premium collected: ' + str(prem) + '\n')
            f.write('Date filled: ' + str(date_obj) + '\n')
            f.write('Exit by: ' + str(exp_obj + timedelta(days=-21)) + '\n')
            f.write('\n')
            f.write(table)
            f.write('\n' + '\n' + '\n' + '#################################################################')
            
        print('Positon succesfully exported to .txt.')
        print('\n')
        continue

    elif command == 'exit':
        break   
