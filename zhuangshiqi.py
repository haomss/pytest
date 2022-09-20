def a(fun):
    def b():
        print("----1")
        fun()
        print("----3")
    return b

@a
def test_aaa():
    print("----2")