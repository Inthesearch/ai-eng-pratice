from fmt_cad import fmt_cad

def test_conversion_single_decimal():
	assert fmt_cad(1234.5)=="$1,234.50"

def test_conversion_zero():
	assert fmt_cad(0)=="$0.00"

def test_conversion_negative():
	assert fmt_cad(-12)=="-$12.00"

def test_conversion_positive():
	assert fmt_cad(12)=="$12.00"

def test_conversion_calculation():
	assert fmt_cad(99-1) == "$98.00"





