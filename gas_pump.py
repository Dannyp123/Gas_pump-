import time


def gas_price(gas_type):
    ''' str -> float

    >>> gas_price('R')
    2.0
    >>> gas_price('Pl')
    2.5
    >>> gas_price('P')
    3.0
    '''
    if gas_type == 'R':
        return 2.0
    if gas_type == 'Pl':
        return 2.5
    if gas_type == 'P':
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
    if pump > 0 and pump <= 8:
        return True
    else:
        return False


def get_zip_code():
    while True:
        z_c = input('\nEnter the zip code on the card. ').strip()
        if is_zip_code(z_c):
            print('You may began pumping gas.')
            return z_c
        else:
            print('Invalid Zipcode....')


def get_pump_number():
    while True:
        pump = int(input('\nWhat pump are you on? '))
        if is_gas_pump(pump):
            print('\nI turned the pump on for you.')
            return pump
        else:
            print('That is not a pump number!')


def print_receipt(type_of_gas, amount, cost, pump_number):
    print('\n\t------Printing Your receipt-------')
    time.sleep(1.5)
    print('\t..................................')
    print('\t..................................')
    print('\t..................................')
    print('\t..................................')
    print('\t..................................')
    print('\t..................................')
    print('\t..................................')
    print('\t..................................')
    print('\t..................................')
    print('\t..................................')

    print("\n\t_______DANNY'S EXPRESS MART_______\n")
    print('              \t 1453 Berkley Ave')
    print("          \t Water Valley, Ms")
    print('           Thank You, Have a blessed day!\n')
    print('        ***********************************')
    print('\n\t. Type of gas:', type_of_gas)
    print('\t-----------------------------------\n')
    print('\t. Cost of gas:', '$', amount)
    print('\t-----------------------------------\n')
    print('\t. Gallons of gas: {} gallons'.format(cost))
    print('\t-----------------------------------\n')
    print('\t. Pump # ' + str(pump_number))
    print('\t-----------------------------------')
    print('\n\t. Total:', '$' + str(amount))
    print('\t-----------------------------------')
    print("\n**Please take your receipt**")


def main():

    print("How you doin, welcome to Danny's Express Mart!!")
    print(
        "\nDanny's Express Mart is owned and operated by your very own Danny P."
    )

    type_of_gas = input(
        '\nDo you want Regular(R), Plus(Pl) or Premium(P)? ').strip()

    pump_number = get_pump_number()

    price = gas_price(type_of_gas)
    if type_of_gas in ['R', 'r']:
        print('\nPrice per gallon for regular is $ 2.00')

    if type_of_gas in ['P', 'p']:
        print('\nprice per gallon for premium is $ 2.50')

    if type_of_gas in ['Pl', 'pi', 'Pi']:
        print('\nprice per gallon for plus is $ 3.00')

    amount = input('\nHow much you paying for? $')

    if amount == 0:
        print('\nGoodbye then')

    cost = round(float(amount) / price)

    print('\nYou can get {} gallons for ${}'.format(cost, amount))

    payment = input(
        '\nHow would you like to pay, now(1) or inside(2)? ').strip().lower()

    if payment == '1':
        print('\nPlease insert card.')
        zip_code = get_zip_code()
    elif payment == '2':
        print('\nPlease pay the person at the counter inside first.')

    receipt = input(
        '\nWould you like a receipt yes(Y) or no(N)? ').strip().lower()

    if receipt in ['Y', 'y']:
        print_receipt(type_of_gas, amount, cost, pump_number)
    elif receipt in ['N', 'n']:
        print("\n\t _______DANNY'S EXPRESS MART______\n")
        print("           \tWater Valley, MS")
        print(
            "\nThank you for shopping at Danny's Express Mart and have a blessed day!\n"
        )

    text = ('\n{}, {}, {}, {}, {}, {}'.format(type_of_gas, amount, cost,
                                              pump_number, payment, receipt))

    with open('gas_pump.txt', 'a') as file:
        file.write(text)


if __name__ == '__main__':
    main()
