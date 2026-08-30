RATE_PER_DATE = 10
MAX_FEE= 500

def calculate_late_fee(days_late):
    fee = days_late*RATE_PER_DATE
    return min(fee,MAX_FEE)
