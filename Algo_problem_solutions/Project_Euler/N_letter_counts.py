#17
def numberWordsCount(n):
    """
    Gets the word count for numbers up to the thousands place.
    """
    total = ''

    unit = {
        1: 'one',
        2: 'two',
        3:'three',
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        19:'nineteen',
        20:'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand'
    }
    words = []
    mult = 0
    numbers = list(range(1,n+1))

    for i in numbers:
        # split the number by digit
        s = str(i)
        s = [int(x) for x in s]
        w = ['' for x in s]

        # for each digit from the end, append the proper unit
        ind = 1
        while ind <= len(s):
            if s[len(s) - ind] in unit:
                if ind == 1:
                    w[len(s)-ind] = unit[s[len(s) - ind]]
                elif ind == 2:
                    if s[len(s) - ind] == 1:
                        combined = s[len(s) - ind]*10 + s[len(s) - ind + 1]
                        w[len(s) - ind + 1] = ''
                        w[len(s)- ind] = unit[combined]
                    else:
                        w[len(s)-ind] = unit[s[len(s) - ind]*10]
                else:
                    w[len(s)-ind] = unit[s[len(s) -ind]] + unit[10**(ind-1)]
                
                if ind == 3:
                    rem = w[len(s)- ind + 1:]
                    rempty = [x == '' for x in rem]
                    if sum(rempty) < len(rem):
                        w[len(s) - ind] += 'and' 
                elif ind == 4:
                    if w[len(s) - ind  + 1] == '':
                        rem = w[len(s)- ind + 1:]
                        rempty = [x == '' for x in rem]
                        if sum(rempty) < len(rem):
                            w[len(s) - ind] += 'and' 
            ind += 1
        
        print(w)
        print(sum([len(x) for x in w]))
        words.extend(w)

    total = ''
    for w in words:
        # print("total=",len(total))
        total += w
    
    print("final=",len(total))

num = int(input())
numberWordsCount(num)
            