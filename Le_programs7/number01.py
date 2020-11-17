# Paul Le
# CS A131
# Nov 17 2020
# Python Practice hw7 num 1


import math


def get_number(data_string: str) -> float:
    user_input = input(data_string)
    user_input = float(user_input)
    while user_input < 0:
        

def main():
    prompt = 'Enter the number of square feet to be painted: '
    user_input = get_number(prompt)
    prompt = 'How much does the paint cost? '
    user_input2 = get_number(prompt)
    surface_ratio = user_input / 112
    paint_required = math.ceil(surface_ratio)
    labor = math.ceil(8 * surface_ratio)
    print('\nThis job requires:')
    print(paint_required, 'gallons of paint')
    print(labor, 'hours of labor')
    paint_cost = user_input2 * paint_required
    labor_cost = 35 * labor
    total = paint_cost + labor_cost
    print('\nCosts for the job:')
    print('Paint: $' + '{:.2f}'.format(paint_cost, 2))
    print('Labor: $' + '{:.2f}'.format(labor_cost, 2))
    print('Total: $' + '{:.2f}'.format(total, 2))

if __name__ == '__main__':
    main()
