#ミュージシャンリスト
list = ["欅坂46","日向坂46","乃木坂46"]

print(list)

# 沖縄の緯度経度
tuple = (127.41,26.13)

print(tuple)

#自分の辞書

dictionary = {"身長" : 173,
              "体重" : 83,
              "好きな色" : "赤"}

print(dictionary)

dic_key = input("キーを入力してください:")

print(dictionary[dic_key])

dictionary[list[0]] = "黒い羊"
dictionary[list[1]] = "キュン"
dictionary[list[2]] = "バレッタ"

dic_key2 = input("キーを入力してください:")

print(dictionary)

print(dictionary[dic_key2])
