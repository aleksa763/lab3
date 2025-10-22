cities_input = input("Введите названия городов через пробел: ")
long_cities = [city for city in cities_input.split() if len(city) > 5]
print(long_cities)
