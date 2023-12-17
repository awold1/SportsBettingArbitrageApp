from app.arbitrage_finder import data_retrieval


def date_test():
    
    assert data_retrieval("NFL", "Week 17") == None

