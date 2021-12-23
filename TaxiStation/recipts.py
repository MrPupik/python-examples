from dataclasses import dataclass
import json
import csv
from os import write


@dataclass
class ReciptType:
    JSON = 'json'
    TEXT = 'text'
    CSV = 'CSV'


class Transcation:
    def __init__(self, product: str, price: int) -> None:
        if len(product) > 30:
            raise ValueError('prodcut name too long. max 30 charecters')
        self.prod = product
        self.price = price

    @property
    def data(self):
        return self.prod, self.price


trans_name = 'transactions'
total_name = 'TOTAL'
deafult_out_file_name = 'my_recipt'


def write_json_recipt(*, out_file_name: str = deafult_out_file_name,
                      transactions: list[Transcation]):
    out_file_name += '.json'
    data = {trans_name: []}
    all_trans = []
    total = 0
    for t in transactions:
        data[trans_name].append({t.prod: t.price})
        total += t.price
    data[total_name] = total

    with open(out_file_name, 'w') as file:
        json.dump(data, file)


def write_text_recipt(*, out_file_name: str = deafult_out_file_name, transactions: list[Transcation]):
    line_size = 50

    def indent_line(first_exp, second_exp):
        first_exp = str(first_exp)
        second_exp = str(second_exp)
        return first_exp + ' '*(line_size-len(first_exp) -
                                len(second_exp)) + second_exp+'\n'
    out_file_name += '.txt'
    total = 0
    with open(out_file_name, 'w') as file:
        file.write('** '+trans_name+' **\n')
        for t in transactions:
            file.write(indent_line(t.prod, t.price))
            total += t.price

        file.write('---- ----\n'+indent_line(total_name, total))


def write_csv_recipt(*, out_file_name: str = deafult_out_file_name, transactions: list[Transcation]):
    out_file_name = out_file_name+'.csv'

    with open(out_file_name, 'w', newline='') as file:
        writer = csv.writer(file, dialect='excel')
        row = ('product', 'price', total_name)
        writer.writerow(row)
        total = 0
        for t in transactions:
            row = (t.prod, t.price)
            writer.writerow(row)
            total += t.price
        row = (None, None, total)
        writer.writerow(row)


_generic_recipt = {
    ReciptType.CSV: write_csv_recipt,
    ReciptType.JSON: write_json_recipt,
    ReciptType.TEXT: write_text_recipt
}


def write_recipt(out_file_name: str,
 transactions: list[Transcation], recipt_type: ReciptType):
    global _generic_recipt
    return _generic_recipt[recipt_type](out_file_name=out_file_name, transactions=transactions)


trans = [Transcation('60 km drive', 400),
         Transcation('30 km drive (partial)', 200)]

# write_text_recipt(transactions=trans)
# write_json_recipt(transactions=trans)
write_csv_recipt(transactions=trans)
