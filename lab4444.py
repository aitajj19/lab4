# 1. Ədədi massiv yaradın və onu fayla yazın.
original_numbers = [3, 5, 7, 9, 11, 13, 2, 4, 6, 8, 10]

with open('numbers.txt', 'w') as file:
    for number in original_numbers:
        file.write(f"{number}\n")

# 2. Fayldan ədədi massivi oxuyun.
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

# 3. 4<x<12 şərtinə uyğun ədədləri yeni fayla yazın və onların cəmini hesablayın.
filtered_numbers = [num for num in numbers if 4 < num < 12]
total_sum = sum(filtered_numbers)

with open('filtered_numbers.txt', 'w') as file:
    for number in filtered_numbers:
        file.write(f"{number}\n")

print(f"Filtered numbers: {filtered_numbers}")
print(f"Total sum: {total_sum}")
