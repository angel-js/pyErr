import math
from this import d



def run():
    my_list = []

    def aniadir_num(lis):
        i = 1
        for i in range(1,11):
            lis.append(i)
        return lis
    
    add_num = aniadir_num(my_list)
    #elevando = elevar_cuadrado(aniadiendo)
    #print(add_num)


    def elevar(lis):
        for i in lis:
            x = pow(i,2)
    
    elevar(my_list)

    my_list = list(range(1,100))
    cuadrado = [ d for d in range(1, 100) 
    if math.sqrt(d) == 8 ]
    print(cuadrado)
    
if __name__ == '__main__':
    run()