# http://tinyurl.com/zfgczj5

st = open("st.txt", "w") #open関数でファイルを開く
st.write("Hi from python") #文字列をファイルに書き込む
st.close() #ファイルを閉じる
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    