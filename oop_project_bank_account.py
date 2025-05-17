from qrcode_generator import *

hassam = BankAccount(5000.00,"hassam")
hussain = BankAccount(300.00,"hussain")

hassam.deposit(500)
hassam.get_balance()

hussain.withdraw(30)
hussain.withdraw(100)

hassam.transfer(65,hussain)

hussain.transfer(11120,hassam)