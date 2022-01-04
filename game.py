import random, os, sys

def pass_exc(func, *args, **kwargs):
    def wrap():
        try:
            func(*args, **kwargs)
        except Exception as error:
            pass

    return wrap

def mopen(*args, **kwargs):
    """Python builtin open function but it has auto close function."""
    with open(*args, **kwargs) as f:
        mopen.content = f.read()
        f.close()
        return mopen

@pass_exc
def cls():
    """Clear terminal texts using command line."""
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def loadff():
    """Asking for open file and load content."""
    from tkinter import (
        Tk,
        messagebox as msgbx,
        filedialog as fdlog,
    )

    root = Tk()
    root.withdraw()

    msgbx.showwarning("경고", "옵션들은 들여쓰기로 구분 되어있어야 합니다!")
    p = fdlog.askopenfilename()

    return str(mopen(p, "r", encoding="utf-8").content)

def stripiter(target: list):
    """Striping all of texts in list."""
    out = []
    for txt in target:
        out.append(
            str(txt)
            .rstrip()
            .lstrip()
        )

    return out

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

    def result(self):
        def Mix(target: list, out: list):   
            for _ in range(len(target)): 
                r = random.choice(target)
                target.remove(r)
                out.append(r)

        b = []

        Mix(self.opts, b)

        out = []

        for i in range(len(self.nbrs)):
            out.append(f"{i + 1}: {b[i]}")

        return out

cls()

cnts = input("옵션의 갯수를 입력하세요\n>>> ")
opts = input("옵션을 입력하세요. 쉼표로 구분해주세요.\n아니면 '파일 불러오기'를 입력하여 파일을 불러오세요.\n>>> ")

if opts == "파일 불러오기":
    opts = loadff().splitlines()
else:
    opts = opts.split(",")

clean = []

clean.extend(stripiter(opts))
opts.clear()
opts.extend(clean)

cls()

bokbulbok = Bokbulbok(int(cnts), opts)
out = bokbulbok.result()
print("결과:\n" + "\n".join(out))
