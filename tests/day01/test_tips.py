import pytest

class NegativeValueError(Exception):
    """Bill and percentage should be positive"""
    pass

# Function que j'implémente 

def total_with_tip(bill, percentage):

    if bill <0:
        raise NegativeValueError("Bill should be positive")
    if percentage<0:
        raise NegativeValueError("Percentage should be positive")
    
    tip = bill* percentage/100
    if tip > 500:
        tip = 500 
    if tip <5:
        tip = 5
    total = bill + tip

    return round(total, 2)

#TDD - Test Driven Development

def test_tip_classic():
    assert total_with_tip(100, 20) == 120

def test_tip_poor_service():
    assert total_with_tip(100, 0) == 100

# Exercice : écrire les tests correspondants : 
# 2. Le tip maximal est de 500€ car il n'existe pas de billet plus gros.
def test_tip_max():
    assert total_with_tip(1000, 51)== 1500
    assert total_with_tip(5000, 15)== 5500
    assert total_with_tip(2000, 26)== 2500
    assert total_with_tip(10000, 12)== 10500

    
# 3. Le plus petit billet étant 5€, il n'est pas possible d'avoir un total plus bas de 5€
def test_min_total():
    assert total_with_tip(1,0) == 5
    assert total_with_tip(2.30,20) == 5
    assert total_with_tip(4,15) == 5
    assert total_with_tip(3,50) == 5

# 4. Vérifer que l'arrondie du total est bien sur deux décimales
def test_two_decimals():
    assert total_with_tip(5, 12.45) == 5.62
    assert total_with_tip(10.12,15) == 11.64
    assert total_with_tip(10, 2.33) == 10.23
    

# 5. Adater votre function d'implementation pour passer les tests

# TODO:Tester les pourcentages -> Exception 

def test_negative_error():
    with pytest.raises(NegativeValueError) as exceptionTips:
        total_with_tip(100, -10)
    assert str(exceptionTips.value) == "Percentage should be positive"

    with pytest.raises(NegativeValueError) as exceptionBills:
        total_with_tip(-20,10)
    assert str(exceptionBills.value) == "Bill should be positive"
