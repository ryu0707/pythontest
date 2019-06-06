list = ["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]

for index, i in enumerate(list):
    print(index,i)

for s in range(25,51):
    print(s)

answer = [1,3,5,7,9]

while True:

    a = input("文字または数値を入力して下さい:")

    if a == "q":
        break

    try:
        a = int(a)
    except ValueError:
        print("数値またはqを入力して下さい")

    if a in answer:
        print("正解")
    else:
        print("不正解")
    
b = [8,19,148,4]
c = [9,1,33,83]

d = []

for t in b:
    for u in c:
        e = t * u
        d.append(e)

print(d)

