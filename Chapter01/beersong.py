word_bottle = ' bottles'
for count in range(99, 0, -1):
    print(count, word_bottle, 'of beer on the wall.')
    print(count, word_bottle, 'of beer.')
    print('Take one down.')
    print('Pass it around.')
    new_count = count - 1
    if new_count == 1:
        word_bottle = 'bottle'
    if new_count == 0:
        print('No more bottles of beer on the wall.')
    else:
        print(new_count, word_bottle, 'of beer on the wall')
    print()
