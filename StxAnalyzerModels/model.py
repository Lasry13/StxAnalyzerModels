import mysql_connector as db


def calculate_interest(data):
    total_amount = data['loan_amount']
    for x in range(data['years_number']):
        total_amount += data['loan_amount'] * data['interest_rate'] / 100
    return [round(total_amount, 2), round(total_amount / data['years_number'] / 12, 2)]


def get_sp_500():
    return db.select('select * from sp_500 limit 2')
