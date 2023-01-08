class A:
    def __init__(self):
        print('A')
        super().__init__()
    
class B(A):
    def __init__(self,):
        super().__init__()
        print('B')

class X:
    def __init__(self,):
        print('X')
        super().__init__()
    

class C(X, B):
    def __init__(self):
        print('C')
        super().__init__()
        
def main():
    c = C()
    print(c)

if __name__ == '__main__':
    main()