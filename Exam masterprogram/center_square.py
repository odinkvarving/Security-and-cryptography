listed_numbers = {}

for number in range(100000, 1000000):

    square = list(str(number ** 2))

    hash = ""
    
    for position in range(4, 7):
        hash += square[position]

    hash = int(hash)

    if hash not in listed_numbers:
        listed_numbers[hash] = 0

    listed_numbers[hash] += 1

sorted(listed_numbers)

total_frequency = 0
for key in listed_numbers:
    total_frequency += listed_numbers[key] - 1

average_frequency = int(total_frequency/len(listed_numbers))
sorted_keys = sorted(listed_numbers.keys())
highest_frequency, lowest_frequeny = sorted_keys[0], sorted_keys[len(sorted_keys) - 1]
frequency_highest, frequency_lowest = listed_numbers[highest_frequency], listed_numbers[lowest_frequeny]
print("The average frequency for any given hash was: %s\nThe hash that had the highest frequency was %s with %s duplicates\nThe hash that has the lowest frequency was %s with %s duplicates" % (average_frequency, highest_frequency, frequency_highest, lowest_frequeny, frequency_lowest))