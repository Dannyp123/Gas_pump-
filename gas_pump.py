def gas_price(gas_type):
    ''' str -> float

    >>> gas_price('regular')
    2.0
    >>> gas_price('premium')
    2.5
    >>> gas_price('plus')
    3.0
    '''
    if gas_type == 'regular':
        return 2.0
    if gas_type == 'premium':
        return 2.5
    if gas_type == 'plus':
        return 3.0


def is_zip_code(zip_str):
    ''' str -> bool 

    >>> is_zip_code('12345')
    True
    >>> is_zip_code('2345689')
    False
    >>> is_zip_code('38965')
    True
    '''
    if zip_str.isdigit() and len(zip_str) == 5:
        return True
    else:
        return False


def is_gas_pump(pump):
    ''' int -> bool 

    >>> is_gas_pump(0)
    False
    >>> is_gas_pump(9)
    True
    '''
    if pump > 0 < 9:
        return True
    else:
        return False


def main():

    print("How you doin, welcome to Danny's Express Mart!!")
    print(
        "\nDanny's Express Mart is owned and operated by your very own Danny P."
    )

    type_of_gas = input('\nDo you want regular, plus or premium?').strip()

    pump = int(input('\nWhat pump are you on?').strip())

    if is_gas_pump(pump):
        print('\nI turned the pump on for you.')

    price = gas_price(type_of_gas)

    if type_of_gas == 'regular':
        print('\nPrice per gallon for regular is $ 2.00')

    if type_of_gas == 'premimum':
        print('\nprice per gallon for premium is $ 2.50')

    if type_of_gas == 'plus':
        print('\nprice per gallon for plus is $ 3.00')

    amount = float(input('\nHow much you paying for? $'))

    if amount == 0:
        print('\nGoodbye then')

    cost = round(amount / price)

    print('\nYou can get {} gallons for ${}'.format(cost, amount))

    payment = input(
        '\nHow would you like to pay, now or inside?').strip().lower()

    if payment in ['now', 'pay now']:
        print('\nPlease insert card.')

        z_c = input('\nEnter the zip code on the card.').strip()

        if is_zip_code(z_c):
            print('You may began pumping gas.')
        else:
            print('Invaild Zipcode....')

    if payment in ['pay inside', 'inside']:
        print('\nPlease pay the person at the counter inside first.')

    receipt = input('\nWould you like a receipt?').strip().lower()

    if receipt in ['yes', 'yeah']:
        print('\n\t---------Printing Your receipt----------')
        print('\t........................................')
        print('\t........................................')
        print('\t........................................')
        print('\t........................................')
        print('\t........................................')
        print('\t........................................')
        print('\t........................................')
        print('\t........................................')
        print('\t........................................')
        print('\t........................................')

        print("\n\t_______DANNY'S EXPRESS MART_______")
        print("          \tWater Valley, Ms")
        print('\n\t....type of gas:', type_of_gas)
        print()
        print('\t....cost of gas:', '$', amount)
        print()
        print('\t....gallons of gas: {} gallons'.format(cost))
        print()
        print('\t....Pump # ' + str(pump))
        print('\n\t....Total:', '$' + str(amount))
        print(
            "\nPlease take your receipt, and thank You for shopping at Danny's Express Mart have a blessed day!"
        )

    if receipt in ['no', 'nope', 'im gucci']:
        print("\n\t _______DANNY'S EXPRESS MART______\n")
        print("           \tWater Valley, MS")
        print(
            "\nThank you for shopping at Danny's Express Mart and have a blessed day!\n"
        )

    text = ('\n{}, {}, {}, {}, {}, {}'.format(type_of_gas, amount, cost, pump,
                                              payment, receipt))

    with open('gas_pump.txt', 'a') as file:
        file.write(text)


if __name__ == '__main__':
    main()
