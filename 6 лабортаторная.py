temperatures = [15.3, 16.8, 18.2, 20.1, 22.5, 25.7, 28.9, 27.6, 24.3, 21.0, 17.5, 14.2, 
                16.1, 17.9, 19.8, 23.4, 26.1, 29.3, 30.5, 28.7, 25.2, 22.8, 18.9, 15.7,
                14.9, 16.5, 19.1, 21.7, 24.8, 27.2]

total_sum = 0
for temp in temperatures:
    total_sum += temp

average_temp = total_sum / len(temperatures)
print(f"Средняя температура за месяц: {average_temp:.1f}°C")