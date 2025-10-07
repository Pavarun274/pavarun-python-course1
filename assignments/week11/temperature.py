"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():
    temp = [25, 26, 31, 30, 29, 28, 31]
    return temp

def analyze_temps(temp_list):
    avg_temp = 0
    highest_temp = max(temp_list)
    lowest_temp = min(temp_list)

    sum = 0
    for temp in temp_list:
        sum += temp
    avg_temp = sum / len(temp_list)
    return (avg_temp, highest_temp, lowest_temp)

def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print("Average: %.2f C" % (avg))
    print(f"Highest: {high} C")
    print("Lowest: ", low, "C")

my_temp = get_temperatures()
analyzed_temps = analyze_temps(my_temp)
display_analysis(analyzed_temps[0], analyzed_temps[1], analyzed_temps[2])