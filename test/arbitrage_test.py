from app.arbitrage_finder import data_retrieval, to_usd


def test_usd():
    assert to_usd(5.0023) == "$5.00"

def test_date():
    
    assert data_retrieval("NFL", "Super Bowl") == None

