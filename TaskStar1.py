# Напишите функцию , которая будет возвращать переданное в качестве параметра n число словами

# Input -> 435467
# Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь


from num2words import num2words

num = int(input('Введите ваше число: '))

print(num2words(num, lang='ru'))
