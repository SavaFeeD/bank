from enum import Enum


class BankName(str, Enum):
    rosbank = 'rosbank'
    sberbank = 'sberbank'