data = []
count = 0
with open('reviews.txt', 'r' ) as f :
    for line in f :
        data.append(line)
        count += 1
        if count % 1000 == 0 :
            print(len(data))
print('檔案讀取完畢，總共有', len(data) , '筆資料')

sum_len = 0
for d in data :
    sum_len += len(d)
avg = sum_len / len(data) 
print('每筆留言的平均長度為',avg,'個字')

new = []
for d in data :
    if len(d) < 100 :
        new.append(d)
print('共有' ,len(new), '筆留言的長度小於100字')