from BigNumber import BigNumber

def test_add_same_signs():
    n1 = BigNumber("222")
    n2 = BigNumber("222")
    assert n1.add(n2).toString() == "444"

    n1 = BigNumber("-222")
    n2 = BigNumber("-222")
    assert n1.add(n2).toString() == "-444"

    n1 = BigNumber("-999")
    n2 = BigNumber("-1")
    assert n1.add(n2).toString() == "-1000"

    n1 = BigNumber("-1")
    n2 = BigNumber("-999")
    assert n1.add(n2).toString() == "-1000"

    n1 = BigNumber("-1654989746897")
    n2 = BigNumber("-222876787685")
    assert n1.add(n2).toString() == "-1877866534582"


def test_add_positive_negative():
    n1 = BigNumber("222")
    n2 = BigNumber("-222")
    assert n1.add(n2).toString() == "0"

    n1 = BigNumber("111")
    n2 = BigNumber("-99")
    assert n1.add(n2).toString() == "12"

    n1 = BigNumber("99")
    n2 = BigNumber("-111")
    assert n1.add(n2).toString() == "-12"

    n1 = BigNumber("222")
    n2 = BigNumber("-111")
    assert n1.add(n2).toString() == "111"

    n1 = BigNumber("1654989746897")
    n2 = BigNumber("-222876787685")
    assert n1.add(n2).toString() == "1432112959212"


def test_add_negative_positive():
    n1 = BigNumber("-222")
    n2 = BigNumber("222")
    assert n1.add(n2).toString() == "0"

    n1 = BigNumber("-111")
    n2 = BigNumber("99")
    assert n1.add(n2).toString() == "-12"

    n1 = BigNumber("-99")
    n2 = BigNumber("111")
    assert n1.add(n2).toString() == "12"

    n1 = BigNumber("-222")
    n2 = BigNumber("111")
    assert n1.add(n2).toString() == "-111"

    n1 = BigNumber("-1654989746897")
    n2 = BigNumber("222876787685")
    assert n1.add(n2).toString() == "-1432112959212"


def test_add_decimal():
    n1 = BigNumber("-222")
    n2 = BigNumber("222.00")
    assert n1.add(n2).toString() == "0"

    n1 = BigNumber("1.00")
    n2 = BigNumber("99")
    assert n1.add(n2).toString() == "100.00"

    n1 = BigNumber("-2")
    n2 = BigNumber("-2.00")
    assert n1.add(n2).toString() == "-4.00"

    n1 = BigNumber("-222.123")
    n2 = BigNumber("111.123")
    assert n1.add(n2).toString() == "-111.000"

    n1 = BigNumber("-1654989746897.123465")
    n2 = BigNumber("222876787685.123465")
    assert n1.add(n2).toString() == "-1432112959212.000000"