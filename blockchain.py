# Firstly our blockchain is empty
blockchain = []


def last_value():
    """ Returns last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Adds new transaction to the blockchain

    :argument :-
        :transaction_amount :- the amount to be added
        :last_transaction :- The last blockchain transaction (default is [1])

    """
    blockchain.append([last_transaction, transaction_amount])


def get_tx_amount():
    """ Gets transaction amount from user input
    Returns the transaction as a float
    """
    return float(input("Enter Transaction Amount: "))


add_value(get_tx_amount())
add_value(get_tx_amount(), last_value())
add_value(get_tx_amount(), last_value())

print(last_value())