# Infinite Precision
Adding big big number!!

# Usage

```python
from BigNumber import BigNumber

num1 = BigNumber("1648976548.65498")
num2 = BigNumber("-4564984945.654")
sum = num1 + num2
print(sum)      # -2916008397
num1 = BigNumber("10")
num2 = BigNumber("10")
sub = num1 - num2
print(sub)      # 0
```

# Unit Test

* Install pytest if haven't

```
pip install pytest
```

* Run test command

```
pytest
```