# This is a Python example with various Clean Code violations

def old_style_function():
    # This function violates multiple Clean Code principles
    user_data = get_user_data()
    processed_data = process_data(user_data)
    result = save_to_db(processed_data)
    return result

def calculate_total(items):
    # Magic number and poor error handling
    total = 0
    for item in items:
        total = total + item.price * 0.15  # 15% magic number
        if item.price < 0:
            # Poor exception handling
            try:
                raise ValueError("Negative price")
            except:
                print("Error occurred")  # Bare except is bad

    return total

def long_and_complex_function(user, items, tax_rate, discount, shipping_address, payment_method):
    # Too many parameters and too long
    if user and user.active:
        if items and len(items) > 0:
            if tax_rate > 0:
                if discount > 0:
                    if shipping_address:
                        if payment_method:
                            # Complex nested logic
                            subtotal = 0
                            for item in items:
                                subtotal += item.price

                            tax = subtotal * tax_rate
                            total = subtotal + tax - discount

                            if shipping_address.country == "USA":
                                total += 10  # Magic number for shipping
                            else:
                                total += 25  # Magic number for international shipping

                            return {
                                'subtotal': subtotal,
                                'tax': tax,
                                'discount': discount,
                                'total': total,
                                'shipping': 10 if shipping_address.country == "USA" else 25
                            }

    return None

def poorly_formatted_function():
    # This function has trailing whitespace and poor formatting
    result = do_something()
    return result

# Hardcoded values make testing difficult
def get_current_date():
    return datetime.now()  # Hard to test - always returns current date