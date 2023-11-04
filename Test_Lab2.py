import Lab2

print("Test_Lab2")

def test_find_min_max():
    floatlist = [4, 16, 28, 10, 8, 17, 1]
    min_value, max_value = Lab2.find_min_max(floatlist)

    assert (min_value == 1)
    assert (max_value == 28)

def test_calc_average():
    floatlist = [4, 16, 28, 10, 8, 17, 1]
    avg_calculation = Lab2.calc_average_temperature(floatlist)

    assert (avg_calculation == 12)

def test_calc_median():
    floatlist = [4, 16, 28, 10, 8, 17, 1]
    median_calc = Lab2.calc_median_temperature(sorted(floatlist))

    assert (median_calc == 10)