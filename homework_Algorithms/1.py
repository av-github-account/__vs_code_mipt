import random


# фиксированная сложность O=n^2
def shuffler(strValue):
    length = len(strValue)
    if length == 0:
        return ("", [])

    # результирующая карта, индекс = индекс символа в в перемешанной версии, значение = индекс в оригинале
    shuffleMap = []
    # карта для отслеживания уже сгенерированных чисел
    randomMap = [False] * length
    i = -1
    while i < length - 1:
        i += 1
        # с каждой итерацией уменьшаем ренж рандом на 1
        randomValue = random.randint(0, length - (i + 1))
        j = -1
        c = -1
        # ищем еще не найденных элемент в карте рандома
        while j < length - 1:
            j += 1
            if randomMap[j] == False:
                c += 1
            if c == randomValue:
                # помечаем найденный элемент
                randomMap[j] = True
                # добавляем сгенерированный индекс к результату
                shuffleMap.append(j)
                break

    # формируем перемешанную версию
    newStr = ""
    for i in shuffleMap:
        newStr += strValue[i]

    return (newStr, shuffleMap)


# восстанавливаем в обратном порядке по карте
def unshuffler(strValue, shuffleMap):
    origStrList = [""] * len(strValue)
    i = -1
    for p in shuffleMap:
        i += 1
        origStrList[p] = strValue[i]
    return "".join(origStrList)


startStr = "fdsfs343уц43254выф32ё1ё4sefsefgsfg"
(shuffleStr, shuffleMap) = shuffler(startStr)
origstr = unshuffler(shuffleStr, shuffleMap)

print(startStr)
print(shuffleStr)
print(shuffleMap)
print(origstr)
