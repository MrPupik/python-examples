class even_number():
    def __init__(self, number):
        if number % 2 == 0:
            self.value = number
        else:
            raise Exception('not even !')

    def half(self):
        return self.value / 2


ev_num = even_number(8)
my_str = 'fldfg'
my_str.upper()

print(ev_num.half())


class client:
    pass


client1 = client()
pass
