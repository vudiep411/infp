class BigNumber:
    def __init__(self, value, negative=None):
        self.negative = negative if negative is not None else value[0] == '-'
        self.value = value[1:] if value[0] == '-' else value

    def __add__(self, other):
        return self.add(other)
    
    def add(self, other):
        if self.negative and not other.negative:
            if self.isBigger(other):
                return BigNumber(self.absoluteSubtract(other)).negate()
            else:
                return BigNumber(other.absoluteSubtract(self))
        elif not self.negative and other.negative:
            if self.isBigger(other):
                return BigNumber(self.absoluteSubtract(other))
            else:
                return BigNumber(other.absoluteSubtract(self)).negate()
        else:
            return BigNumber(self.abosoluteAdd(other), self.negative)

  
      
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

  
    def negate(self):
        return BigNumber(self.value, not self.negative)

  
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

    def toString(self):
        if len(self.value) == 1 and self.value[0] == '0':
            return '0'
        else:
            return '-' + self.value if self.negative else self.value
