import luhn  

# Luhn wrapoper function
def is_credit_card_valid(card_number):    
    return luhn.verify(card_number)

# Test definitions
def run_tests():

    assert is_credit_card_valid("4111111111111111"), '4111111111111111 should pass but did not'

    assert is_credit_card_valid("5105105105105100"), '5105105105105100 should pass but did not'

    assert not is_credit_card_valid("134"), '134 should not pass but did'

    assert not is_credit_card_valid("1234567890123456"), '1234567890123456 should not pass but did'

    assert not is_credit_card_valid("000000000000"), 'This is a bad test and we will get an error message'

run_tests() 