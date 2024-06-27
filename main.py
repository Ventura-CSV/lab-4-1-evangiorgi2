def main():

    N = int(input('Enter the number N: '))
    result = []
    for i in range(0, N + 1):
        power = 2 ** i
        result.append(power)
    
    print (result)
    return result


if __name__ == '__main__':
    main()
