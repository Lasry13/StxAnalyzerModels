
def calculate_interest(data):
    total_amount = data['amount']
    for x in range(data['years_number']):
        total_amount += data['amount'] * data['interest_rate'] / 100
    total_return = round(total_amount, 2)
    profit = round(total_return - data['amount'], 2)
    return {'total_return': total_return, 'profit': profit}
