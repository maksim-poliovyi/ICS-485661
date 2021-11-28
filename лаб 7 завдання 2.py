import pylab

filePath = "https://github.com/maksim-poliovyi/ICS-485661/blob/main/%D0%BB%D0%B0%D0%B1%207%20%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F%202.txt"
file1 = open(filePath, "r", encoding='UTF-8').read().lower().split()
print(file1)
symbols = []

for word in file1:
    for symbol in word:
        symbols.append(symbol)  

symbols.sort()
frequency = {}

for item in symbols:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1

keys, values = zip(*frequency.items())

pylab.bar(keys, values)
pylab.show()
© 2021 GitHub, Inc.
Terms