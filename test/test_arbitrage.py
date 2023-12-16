from app.arbitrage_finder import date_conversion, arbitrage_calculator, to_usd

def arbitrage_math_test():
    test_var1 = ("Test", 1.8, "Test")
    test_var2 = ("Test", 2.3, "Test")
    assert arbitrage_calculator(test_var1,test_var2,100) == (f"Bet placed on home team: {to_usd(56.10)}, Bet placed on away team: {to_usd(43.90)}, Total Profit if Home Team Wins: {to_usd(.98)}, Total Profit if Away Team Wins: {to_usd(.98)}")

def date_test():
    
    assert date_conversion("2023-12-20T01:00:00Z") == 1703034000    

