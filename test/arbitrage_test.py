from app.arbitrage_finder import data_retrieval, date_conversion


def date_test():
    
    assert type(data_retrieval("NFL", "Week 15")) == type(list)

