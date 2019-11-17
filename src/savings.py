def save(last_week, this_week):
    water_price = (0.7039 + 0.7469 + 0.7098)/3
    return (water_price * (last_week-this_week))
