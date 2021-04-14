"""
%d - retorna o dia do mês no formato 01, 02 ... 30, 31
%m - retorna o mês com dois dígitos 01, 02 ... 11, 12
%Y - retorna o ano com quatro dígitos 2021
"""

from datetime import date, datetime


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')  # converte data pra string (dd/mm/yyyy)
    # strftime(formato desejado)


def str_para_date(data: str):
    return datetime.strptime(data, '%d/%m/%Y')  # recebe string e transforma em data
    # strptime(string, formato desejado)


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'
