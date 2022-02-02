def fibonacci(numberOfFibonacci):
    print(type(numberOfFibonacci))
    if isinstance(numberOfFibonacci, int):
        counter = 0
        fibNumberCounter = 0
        fibbonaciNumbers = [0, 1]
        while counter != numberOfFibonacci:
            previousNumber = fibbonaciNumbers[counter]
            lastNumber  = fibbonaciNumbers[counter + 1]
            newIndex = lastNumber + previousNumber
            fibbonaciNumbers.append(newIndex)
            print(fibbonaciNumbers[counter])
            counter = counter + 1
        return fibbonaciNumbers

print(fibonacci(10))
