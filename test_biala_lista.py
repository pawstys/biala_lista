from datetime import datetime
from biala_lista import ObliczSkrot
from biala_lista import UtworzSkrotNRB

# Sprawdzenie przykładów podanych w specyfikacji technicznej:

def test_ObliczSkrot():
    klucz = "f8b915776eab735fdd10266b2e66068447904852b82c30eeb6de30703a087eb17ea4c4a37630494607194ddb9354c1211bd984fb5f4d9cff95f5a24ed52065e7"
    assert ObliczSkrot(datetime(2019,10,18).date(), '1435721230','34102012221314181237774212', 5000)  == klucz
    klucz = "d3dfed802034d198b484c9f19e43c1b7540c3a7808503d01a5ccedbb169012bee6a77979ed46b27f5de2bee0d22eb7c7ca9522dfa92e465999e68e9906e01425"
    assert ObliczSkrot(datetime(2019,10,18).date(), '1134679109','XX72123370XXXXXXX022XXXXXX', 5000)  == klucz

def test_UtworzSkrotNRB():
    skrot = 'XX72123370XXXXXXX022XXXXXX'
    assert UtworzSkrotNRB('20721233708680000022663112', 'XX72123370XXXXXXXYYYXXXXXX') == skrot
