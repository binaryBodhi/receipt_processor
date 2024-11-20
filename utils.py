import math
from datetime import datetime


# FUNCTION TO CALCULATE POINTS AWRDED TO RECEIPT
def calculate_points(receipt):
    points = 0

    points += sum(1 for char in receipt.retailer if char.isalnum())

    total_float = float(receipt.total)
    if total_float.is_integer():
        points += 50
    if total_float % 0.25 == 0:
        points += 25

    num_items = len(receipt.items)
    points += (num_items // 2) * 5
    
    for item in receipt.items:
        description_length = len(item.shortDescription.strip())
        if description_length % 3 == 0:
            item_price = float(item.price)
            points += math.ceil(item_price * 0.2)

    purchase_date = datetime.strptime(receipt.purchaseDate, "%Y-%m-%d")
    if purchase_date.day % 2 != 0:
        points += 6

    purchase_time = datetime.strptime(receipt.purchaseTime, "%H:%M")
    if purchase_time.hour == 14 or (purchase_time.hour == 15 and purchase_time.minute == 0):
        points += 10

    return points