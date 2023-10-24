import statistics


def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32")


def get_user_input():
    stringValue = input()
    stringList = stringValue.split(",")
    floatList = list(map(float, stringList))
    # print("List of floats - " + str(floatList))
    return floatList


def calc_average_temperature(floatList):
    avgTemp = sum(floatList) / len(floatList)
    return avgTemp


def find_min_max(floatList):
    min_temp = min(floatList)
    max_temp = max(floatList)
    return min_temp, max_temp

def sort_temperature(floatList):
    sorted_temp = sorted(floatList)
    return sorted_temp


def calc_median_temperature(sorted_temp):
    median_temp = statistics.median(sort_temperature())
    return median_temp

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    minVal, maxVal = find_min_max(num_list)
    print("Min temperature is " + str(minVal))
    print("Max temperature is " + str(maxVal))
    sortedTemp = sort_temperature(num_list)
    print("Temperatures in ascending order is " + str(sortedTemp))
    medianTemp = calc_median_temperature(num_list)
    print("Median of temperatures is " + str(medianTemp))

if __name__ == "__main__":
    main()
