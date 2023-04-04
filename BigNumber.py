class BigNumber:
    def __init__(self, value, negative=None, decimal=None):
        self.negative = negative if negative is not None else value[0] == '-'
        self.value = value[1:] if value[0] == '-' else value
        if decimal is None:
            self.decimal = len(value) - value.find('.') - 1 if value.find('.') != -1 else 0
        else:
            self.decimal = decimal
        self.value = self.value.replace('.', '')


    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self) -> str:
        return self.toString()


    def add(self, other):
        decimal = self.getBiggerDecimal(other)
        self.padDecimal(other)
        if self.negative and not other.negative:
            if self.isBigger(other):
                return BigNumber(value=self.absoluteSubtract(other), decimal=decimal).negate()
            else:
                return BigNumber(value=other.absoluteSubtract(self), decimal=decimal)
        elif not self.negative and other.negative:
            if self.isBigger(other):
                return BigNumber(value=self.absoluteSubtract(other), decimal=decimal)
            else:
                return BigNumber(value=other.absoluteSubtract(self), decimal=decimal).negate()
        else:
            return BigNumber(value=self.abosoluteAdd(other), negative=self.negative, decimal=decimal)

    def subtract(self, other):
        decimal = self.getBiggerDecimal(other)
        self.padDecimal(other)
        if self.negative and not other.negative:
            return BigNumber(value=self.abosoluteAdd(other), negative=True, decimal=decimal)
        elif not self.negative and other.negative:
            return BigNumber(value=self.abosoluteAdd(other), negative=False, decimal=decimal)
        elif self.negative and other.negative:
            if self.isBigger(other):
                return BigNumber(value=self.absoluteSubtract(other), negative=True, decimal=decimal)
            else: 
                return BigNumber(value=other.absoluteSubtract(self), negative=False, decimal=decimal)
        else:
            if self.isBigger(other):
                return BigNumber(value=self.absoluteSubtract(other), negative=False, decimal=decimal)
            else:           
                return BigNumber(value=other.absoluteSubtract(self), negative=True, decimal=decimal)

    def multiply(self, other):
        decimal = self.decimal + other.decimal
        if (self.negative and other.negative) or (not self.negative and  not other.negative):
            return BigNumber(other.absoluteMultiply(self), negative=False, decimal=decimal)
        else:
            return BigNumber(other.absoluteMultiply(self), negative=True, decimal=decimal)

    def abosoluteAdd(self, other):
        result = ""
        carry = 0
        self_idx = len(self.value) - 1
        other_idx = len(other.value) - 1
        while self_idx >= 0 or other_idx >= 0:
            sum = carry + (int(self.value[self_idx]) if self_idx >= 0 else 0) + (int(other.value[other_idx]) if other_idx >= 0 else 0)
            result = str(sum % 10) + result
            carry = sum // 10
            self_idx -= 1
            other_idx -= 1
      
        if carry > 0:
            result = str(carry) + result
        return result

    def absoluteSubtract(self, other):
        result = ""
        borrow = 0
        self_idx = len(self.value) - 1
        other_idx = len(other.value) - 1

        while self_idx >= 0 or other_idx >= 0:
            diff = (int(self.value[self_idx]) if self_idx >= 0 else 0) - (int(other.value[other_idx]) if other_idx >= 0 else 0) - borrow
            borrow = 1 if diff < 0 else 0
            if diff <= 0 and self_idx == 0 and other_idx == 0:
                break
            result = (str(10 + diff) + result) if diff < 0 else str(diff) + result
            self_idx -= 1
            other_idx -= 1

        while result[0] == '0' and len(result) > 1:
            result = result[1:]

        return result if result else '0'

    def absoluteMultiply(self, other):
        result = "0"
        carry = 0
        base = ""
        other_idx = len(other.value) - 1
        while other_idx >= 0:
            self_idx = len(self.value) - 1
            temp = ""
            while self_idx >= 0:
                product = int(self.value[self_idx]) * int(other.value[other_idx]) + carry
                temp = str(product % 10) + temp
                carry = product // 10
                self_idx -= 1
            if carry > 0:
                temp = str(carry) + temp
                carry = 0
            temp += base
            base += '0'
            result = (BigNumber(result, negative=False) + BigNumber(temp, negative=False)).value
            other_idx -= 1
        return result
  
    def negate(self):
        return BigNumber(self.value, not self.negative, decimal=self.decimal)

  
    def isBigger(self, other):
        if len(self.value) > len(other.value):
            return True
        elif len(self.value) < len(other.value):
            return False
        else:
            i = 0
            while i < len(self.value):
                if self.value[i] > other.value[i]:
                    return True         
                elif self.value[i] < other.value[i]:
                    return False
                i += 1
        return False


    def getBiggerDecimal(self, other):
        return max(self.decimal, other.decimal)


    def padDecimal(self, other):
        pads = abs(self.decimal - other.decimal)
        if pads > 0:
            i = 0
            if self.decimal > other.decimal:
                while i < pads:
                    other.value += '0'
                    i += 1
            else: 
                while i < pads:
                    self.value += '0'
                    i += 1

    def toString(self):
        if len(self.value) == 1 and self.value[0] == '0':
            return '0'
        else:
            if self.decimal == 0:
                return '-' + self.value if self.negative else self.value
            else:
                decimal_idx = len(self.value) - self.decimal
                negative = '-' if self.negative else ''
                return negative + self.value[:decimal_idx] + '.' + self.value[decimal_idx:]
