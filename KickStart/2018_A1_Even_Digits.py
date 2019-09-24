class EvenDigits():
    def is_even_digits(self, a):
        for c in str(a):
            if int(c) % 2 != 0:
                return False
        return True

    def to_even_digits(self, a):
        # a : int number
        if self.is_even_digits(a): return int(0)
        i = 1
        while True:
            if self.is_even_digits(a+i) or self.is_even_digits(a-i):
                return i
            else:
                i += 1
    def to_even_digits_(self, a):
        # todo
