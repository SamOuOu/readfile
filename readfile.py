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