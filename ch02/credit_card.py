class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, acnt, limit):
        """Create a new credit card instance.

        The initial balance is zero

        customer the name of the customer (e.g. 'John Bowman')
        bank     the name of the bank (e.g. 'California Savings')
        acnt     the account identifier (e.g.,'3232 2332 3493 3432')
        limit    credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer."""
        return self._customer

    def get_bank(self):
        """Return name of the bank"""
        return self._bank

    def get_account(self):
        """Return the card identifier (typically stored as a string)"""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed; False if charge was denied.
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr,
                 call_count = 0, min_payment_percent = .05, late_fee = 5):
        """Create a new predatory credit card instance.

        The initial balance is zero

        customer the name of the customer (e.g. 'John Bowman')
        bank     the name of the bank (e.g. 'California Savings')
        acnt     the account identifier (e.g.,'3232 2332 3493 3432')
        limit    credit limit (measured in dollars)
        apr      annual percentage rate (e.g. 0.0825 for 8.25% APR)
        """

        SURCHARE = 1

        super().__init__(customer, bank, acnt, limit)       # call super constructor
        self._apr = apr
        self._call_count = call_count
        self._cum_payment = 0
        self._min_payment_percent = min_payment_percent
        self._late_fee = late_fee

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed;
        False if charge was denied and assess $5 fee.
        """

        self._call_count += 1
        if self._call_count <= 10:
            success = super().charge(price) # call inheried method
        else:
            success = super().charge(price + SURCHARE) # call inheried method
        if not success:
            self._balance += 5          # assess penalty
        return success                  # caller expects to return value

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount
        self._cum_payment += amount

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._cum_payment < self._balance * self._min_payment_percent:
            self._balance += self._late_fee

        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor.
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor



if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings',
                           '5391 0375 9387 5309', 2500) )
    wallet.append(CreditCard('John Bowman', 'California Federal',
                           '3485 0399 3395 1954', 3500) )
    wallet.append(CreditCard('John Bowman', 'California Finance',
                           '5391 0375 9387 5309', 5000) )

    for val in range(1,2000):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
              wallet[c].make_payment(100)
              print('New balance =', wallet[c].get_balance())
    print()










