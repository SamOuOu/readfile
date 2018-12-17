data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完畢，共有', len(data), '筆資料')

sum_len = 0
for length in data:
    sum_len = (sum_len + len(length))
print(sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print(len(new))            


good = []
for d in data:
    if 'good' in d:
        good.append(d)
print(len(good))        

#文字計數

word_count = {}
for d in data:
    words = d.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1  #新增新的key進字典
for word in word_count:
    if word_count[word] > 1000000:
        print(word, word_count[word])
print(len(word_count))

while True:    
    word = input('請輸入要查詢的字: ')
    if word == 'q':
        break
    if word in word_count :
        print(word, '出現', word_count[word], '次')
    else:
        print(word, '沒有出現過')

print('88')

