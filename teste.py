from models.cliente import Cliente
from models.conta import Conta

douglas = Cliente('Douglas', 'douglas@doug.com', '123.456.789-10', '15/03/2021')
contad = Conta(douglas)

print(contad)
