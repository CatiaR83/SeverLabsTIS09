 # matricula (str), marca, modelo, data
# 10-XY-20,Opel,Corsa XL,2019-10-15
# 20-PQ-15,Mercedes,300SL,2017-05-31

# Menu
#       1 - Listar Viaturas
#       2 - Pesquisar Viaturas
#       3 - Adicionar Viatura
#       4 - Remover Viatura
#       5 - Actualizar Catálogo
#       6 - Recarregar Catálogo
#       T - Terminar
# 
#       Opção >> 

from decimal import Decimal as dec
from pickle import NONE
import csv
import subprocess
import sys
import datetime
from typing import TextIO

CSV_DEFAULT_DELIM = ','
DEFAULT_INDENTATION = 3

VIATURAS_TYPES = {
    'OC': 'Opel',
    'MC': 'Mercedes',
    'FD': 'Ford'
}

class Viatura:
    def __init__(
            self, 
            matricula: str, 
            marca: str, 
            modelo: str, 
            data: datetime,
    ):
        self.marca = None
        for viat in VIATURAS_TYPES:
            if VIATURAS_TYPES[viat].__eq__(marca):
                self.marca = viat
        if self.marca is None:
            raise InvalidViaturaType(f'Tipo da viatura ({marca}) desconhecida')

        self.matricula = matricula
        self.modelo = modelo
        self.data = data

    @property
    def desc_marca(self) -> str:
        return VIATURAS_TYPES[self.marca]
    
    def desc_for_file(self) -> str:
        return f'{self.matricula},{self.desc_marca},{self.modelo},{self.data.strftime("%Y-%m-%d")}'
    
    def __str__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}[matricula = {self.matricula}, marca = "{self.desc_marca}", modelo = "{self.modelo}", data ="{self.data.strftime("%Y-%m-%d")}"]'
    #:

class CatalogoViaturas:
    def __init__(self):
        self._viats = {}
    #:

    def pesquisa(self, matricula) -> 'Viatura':
        for viat in self._viats.values():
            if matricula == viat.matricula:
                return viat
    #:

    def append(self, viat: Viatura):
        if viat.matricula in self._viats:
            raise DuplicateValue(f'Já existe uma viatura com a matricula {viat.matricula} no catálogo')
        self._viats[viat.matricula] = viat
    #:

    def remove(self, matricula: str):
        if self._viats[matricula]:
            del self._viats[matricula]
        else:
            raise DoesNotExistViatur(f'Não existe uma viatura com a matricula {viat.matricula} no catálogo')
    #:

    def _dump(self):
        for viat in self._viats.values():
            print(viat)
        #:
    #:

class InvalidViaturaType(ValueError):
    pass
#:

class DoesNotExistViatur(ValueError):
    pass
#:


class DuplicateValue(Exception):
    pass
#:

def main() -> None:
    viaturas = CatalogoViaturas()
    viaturas.append(Viatura('20-MM-55', 'Opel', 'Corsa XL', datetime.datetime(2019, 5, 23))) #datetime.datetime(2019, 5, 23)))
    viaturas.append(Viatura('55-SS-99', 'Mercedes', '300SL', datetime.datetime(2019, 5, 23))) #datetime.datetime(2021, 10, 26)))
    viaturas.append(Viatura('78-TY-88', 'Mercedes', '300SL', datetime.datetime(2019, 5, 23)))#datetime.datetime(2020, 8, 17)))
    continuaExecutar=True

    while continuaExecutar:
        print('#            Menu')
        print('#       1 - Listar Viaturas')
        print('#       2 - Pesquisar Viaturas')
        print('#       3 - Adicionar Viatura')
        print('#       4 - Remover Viatura')
        print('#       5 - Actualizar Catálogo')
        print('#       6 - Recarregar Catálogo')
        print('#       T - Terminar')
        print('# ')
        opcao = str(input('#       Opção >> '))
        match opcao:
            case '1':
                viaturas._dump()
            
            case '2':
                print('Matricula da viatura')
                matri = str(input())
                viatura = viaturas.pesquisa(matri)
                print(viatura)
            
            case '3':
                print('Matricula da viatura')
                matricula = str(input())
                print('Marca da viatura')
                marca = str(input())
                print('Modelo da viatura')
                modelo = str(input())
                data = input('Data da viatura no formato YYYY-MM-DD\n')
                year, month, day = map(int, data.split('-'))
                datafinal = datetime.date(year, month, day)
                viaturas.append(Viatura(matricula, marca, modelo, datafinal))
            
            case '4':
                print('Matricula da viatura')
                matricula = str(input())
                viaturas.remove(matricula)

            case '5':
                with open('viaturas.csv', 'w') as csvfile:
                    fields = ['matricula', 'marca', 'modelo', 'data']
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    for viatura in viaturas._viats:
                        writer.writerow({'matricula': f'{viatura.matricula}', 'marca': f'{viatura.marca}', 'modelo' : f'{viatura.modelo}', 'data': f'{viatura.data.strftime("%Y-%m-%d")}'})

            case '6':
                viaturas = CatalogoViaturas()
                with open('viaturas.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        year, month, day = map(int, row['data'].split('-'))
                        datafinal = datetime.date(year, month, day)
                        viaturas.append(Viatura(row['matricula'], row['marca'], row['modelo'],datafinal))

            case 'T':
                continuaExecutar = False
#:

if __name__ == '__main__':
    main()
#: