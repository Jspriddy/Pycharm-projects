import datetime
import sqlite3
import pytz

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, account TEXT NOT NULL,"
           "amount INTEGER NOT NULL, PRIMARY KEY (time, account))")


class Account(object):

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES (?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            new_balance = self._balance + amount  # We store new_balance in a new variable
            # because we don't want to update self._balance if the transaction fails
            deposit_time = pytz.utc.localize(datetime.datetime.utcnow())
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            db.commit()
            self._balance = new_balance
            print("{:.2f} deposited".format(amount / 100))
            self.show_balance()
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("{:.2f} withdrawn".format(amount / 100))
            self.show_balance()
            return amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    Jobathan = Account("Jobathan")
    # Jobathan.deposit(30)
    # Jobathan.deposit(970)
    Jobathan.withdraw(1000)
    Jobathan.show_balance()

    Frodo = Account("Frodo", 2000)
    Henry = Account("Henry", 10000)
    Maggie = Account("Maggie", 300000)
    # Maggie.deposit(10)

    db.close()
