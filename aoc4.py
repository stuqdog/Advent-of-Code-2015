import md5

key = 'yzbqklnj'
key_sum = 1

while True:
    check = key + str(key_sum)
    test = md5.new(check).hexdigest()
    if all(test[x] == '0' for x in range(6)):
        break
    key_sum += 1

print(key_sum)
