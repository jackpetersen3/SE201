#variable declaration
wordList = []
flag = 0
found = 0

def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

         # Recursively call each half of the list
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
                if int(left[i][1]) > int(right[j][1]):
                        array[k] = left[i]
                        i += 1
                else:
                        array[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

        while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1


with open('neuromancer.txt') as reader:
    for line in reader:
        for word in line.split():
            if flag == 0:
                wordList.append([(word.lower()), (1)])
                flag = 1
            else:
                for i in range(0 , len(wordList)):
                    if  word.lower() == wordList[i][0]:
                        wordList[i][1] += 1
                        found = 1
                        break
                if found != 1:
                    wordList.append([(word.lower()), (1)])
                found = 0       

    mergeSort(wordList)
    for i in range(0, 24):
        print(wordList[i][0], wordList[i][1])