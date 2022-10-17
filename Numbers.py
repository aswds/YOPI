def replaceStr(string):
    return str(string).replace('\n', '')


class Numbers:
    number = 0
    count = 0

    def __init__(self, number, count ):
        self.number = number
        self.count = count

    def __str__(self):

        return f'\n{self.number:>5}\t\t || \t\t {self.count:>5}'
