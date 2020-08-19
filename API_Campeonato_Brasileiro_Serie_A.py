# API - Campeonato Brasileiro Série A
import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Exibe à classificação do Campeonato Brasileiro.')
parser.add_argument('--serie', help='Informe à série a ser exibida a, b, c ou d', default='a')
args = parser.parse_args()

clubs = []

request = requests.get('https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-'+args.serie.lower())
soup = BeautifulSoup(request.text, 'html.parser')
info = soup.find_all('tr', class_='expand-trigger')

for td in info:
    clubs.append(td.get_text()[3:70].split('\n'))

print(f'\n{"_" * 103}')
print(f'\033[32m\n{" Campeonato Brasileiro Série "+args.serie.upper():^102}\033[m')
print(f'{"_" * 103} \n')
print(f'\033[33mClassificação                                    P    J    V    E    D   GP   GC    SG    CA   CV    %\033[m\n')

for club in clubs:
    if club in clubs[0:4]:
        print(f'{club[0]:>3}  {club[1]:>2}  \033[36m{club[3]:<30}\033[m\t\t{club[5]:>2}   {club[6]:>2}   {club[7]:>2}'
              f'   {club[8]:>2}   {club[9]:>2}   {club[10]:>2}   {club[11]:>2}   {club[12]:>3}   {club[13]:>3}'
              f'   {club[14]:>2}   {club[15]:>3}')
    elif club in clubs[4:16]:
        print(f'{club[0]:>3}  {club[1]:>2}  {club[3]:<30}\t\t{club[5]:>2}   {club[6]:>2}   {club[7]:>2}'
              f'   {club[8]:>2}   {club[9]:>2}   {club[10]:>2}   {club[11]:>2}   {club[12]:>3}   {club[13]:>3}'
              f'   {club[14]:>2}   {club[15]:>3}')
    else:
        print(f'{club[0]:>3}  {club[1]:>2}  \033[31m{club[3]:<30}\033[m\t\t{club[5]:>2}   {club[6]:>2}   {club[7]:>2}'
              f'   {club[8]:>2}   {club[9]:>2}   {club[10]:>2}   {club[11]:>2}   {club[12]:>3}   {club[13]:>3}'
              f'   {club[14]:>2}   {club[15]:>3}')

print(f'\n{"_" * 103} \n')
print('{:^94}'.format(" B\'H\'A - Bendito seja o Pai que está nos céus! "))
print(f'{"_" * 103} \n')
