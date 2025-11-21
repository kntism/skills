// This is a JavaScript example with various Clean Code violations
function oldStyleFunction() {
    // This function does too many things and has poor naming
    var user_data = get_user_data();
    var processed_data = process_data(user_data);
    var result = save_to_db(processed_data);
    return result;
}

function calculate_total(items) {
    // Magic number and poor error handling
    var total = 0;
    for (var i = 0; i < items.length; i++) {
        total = total + items[i].price * 0.15; // 15% magic number
        if (items[i].price < 0) {
            // Empty catch block is bad
            try {
                throw new Error("Negative price");
            } catch (e) {
                console.log("Error occurred");
            }
        }
    }
    return total;
}

function longAndComplexFunction(user, items, taxRate, discount, shippingAddress, paymentMethod) {
    // Too many parameters and too long
    if (user && user.active) {
        if (items && items.length > 0) {
            if (taxRate > 0) {
                if (discount > 0) {
                    if (shippingAddress) {
                        if (paymentMethod) {
                            // Complex nested logic
                            var subtotal = 0;
                            for (var i = 0; i < items.length; i++) {
                                subtotal += items[i].price;
                            }

                            var tax = subtotal * taxRate;
                            var total = subtotal + tax - discount;

                            if (shippingAddress.country === "USA") {
                                total += 10; // Magic number for shipping
                            } else {
                                total += 25; // Magic number for international shipping
                            }

                            return {
                                subtotal: subtotal,
                                tax: tax,
                                discount: discount,
                                total: total,
                                shipping: shippingAddress.country === "USA" ? 10 : 25
                            };
                        }
                    }
                }
            }
        }
    }
    return null;
}

// This function has trailing whitespace and poor formatting
function poorlyFormattedFunction() {
    var result = doSomething();
    return result;
}