def file(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            separator = line.split(';')
            number1 = list(map(int, separator[0].split()))
            n = sum(number1) // len(number1)
            m = sum(number1) % len(number1)
            number2 = list(map(int, separator[1].split()))
            if number2[0] == n and number2[1] == m:
                print(line.strip(), True)
            else:
                print(line.strip(), False)



print(file("C:/Users/HP/Documents/a-level/MODULE1/strings.txt"))


# output
# 2 4 5;3 2 True
# 3 2 1;2 0 True
# 6 5 2 1 2;3 1 True
# 7 3;3 4 False
# 4 6 8;6 0 True


    
