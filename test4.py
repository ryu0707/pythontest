x = "カミュ"

print(x[0])
print(x[1])
print(x[2])

what = input("入力1:")
who = input("入力2:")

sentence = "私は昨日{}を書いて、{}に送った！".format(what,who)

print(sentence)

y = "aldous Huxley was born in 1894.".capitalize()

print(y)

z = "どこで？ だれが？ いつ？".split(" ")

print(z)

a = ["The","fox","jumped","over","the","fence","."]

b = " ".join(a).replace(" .",".")

print(b)

c = "A screaming comes across the sky.".replace("s","$")

print(c)

first_index = "Hemingway".index("m")

print(first_index)

d = "three" + "three" + "three"
e = "three" * 3

print(d)
print(e)

f = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"

print(f[0:11])

