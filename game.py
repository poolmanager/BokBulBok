import random, os, sys

from contextlib import closing

def clear():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def load_from_file():
    import tkinter, tkinter.messagebox, tkinter.filedialog

    root = tkinter.Tk()
    root.withdraw()

    tkinter.messagebox.showwarning("경고", "파일에서 불러오는 옵션들은 들여쓰기로 구분이 되어있어야 합니다!")
    
    t = tkinter.filedialog.askopenfilename()

    with closing(open(t, "r", encoding="utf-8")) as f:
        return f.read().splitlines()

class Bokbulbok:
    def __init__(self, number: int, options: list):
        if len(options) <= 1:
            raise ValueError

        nbrs = []
        for i in range(number):
            nbrs.append(str(i))

        if len(nbrs) != len(options):
            raise

        if len(nbrs) <= 1:
            raise ValueError

        for num in nbrs:
            if not str(num).isnumeric():
                raise TypeError

        self.nbrs = nbrs
        self.opts = options

    def start(self):
        def random_get_and_delete(ValueList: list):    
            r = random.choice(ValueList)
            ValueList.remove(r)
            return r

        b = []

        for i in range(len(self.nbrs)):
            b.append(random_get_and_delete(self.opts))

        for i in range(len(self.nbrs)):
            if i == 0:
                print("결과: ")

            print(f"{i + 1}: {b[i]}")

        while True:
            sys.stdout.write("\b\r")

clear()
_cnts = input("옵션의 갯수를 입력하세요\n>>> ")

_opts = input("옵션을 입력하세요. 쉼표로 구분해주세요.\n아니면 '파일 불러오기'를 입력하여 파일을 불러오세요.\n>>> ")

if _opts == "파일 불러오기":
    _opts = load_from_file()
else:
    _opts = _opts.split(",")

_striped_opts = []

for s in _opts:
    _striped_opts.append(s.lstrip().rstrip())

_opts.clear()
_opts.extend(_striped_opts)

clear()

base = Bokbulbok(int(_cnts), _opts)
base.start()
