# python3

def build_heap(data):
    swaps = []
    izmers = len(data)
    for i in (range(izmers, -1, -1)):
        j = i
        while True:
            mazakaVertiba = j
            kreisi = j*2 + 1
            labi = kreisi + 1
            
            if(kreisi >= izmers):
                break
            if (data[j] > data[kreisi]):
                mazakaVertiba = kreisi

            if (labi < izmers and data[j] > data[labi] and data[kreisi] > data[labi]):
                mazakaVertiba = labi

            if (mazakaVertiba == j):
                break
            data[j], data[mazakaVertiba] = data[mazakaVertiba], data[j]
            swaps.append([j, mazakaVertiba])
            j = mazakaVertiba


    #print(data)
    return swaps


def main():
    text = input()
    if text[0] == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif text[0] == "F":
        text = "tests/" + input()
        fails = open(text)
        text = fails.read()
        for index, cip in enumerate(text.split()):
            if(index == 0):
                n = int(cip)
                data = list()
                continue
            data.append(int(cip))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
