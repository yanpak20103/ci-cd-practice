def calculate_discount(price, discount):
    if price < 0 or discount < 0:
        raise ValueError("Цена и скидка должны быть положительными!")

    return price - (price * discount / 100)


def is_valid_email(email: str) -> bool:
    return '@' in email and '.' in email
