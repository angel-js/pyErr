#Defino una función
def run():
    my_list = [1,"Hello", True, 4.5]
    my_dict = {"firstname": "Angel", "Lastname": "Serrano"}

#Lista con diccionarios Anidados
super_list = [
    {"firstname": "Facu", "Lastname": "Aravena"},
    {"firstname": "Maria", "Lastname": "Pacal"},
    {"firstname": "Pepe", "Lastname": "Ravet"},
    {"firstname": "Juan", "Lastname": "Montilla"}
]

# Diccionario con listas anidadas
super_dict ={
    "natural_nums":[0,1,2,3,4,5],
    "floats_nums":[0.1, 0.2, 0.3, 0.4],
    "impar_nums":[1,3,5,7,9],
    "par_nums":[2,4,6,8,]
}

# Correr el diccionario
for key, value in super_dict.items():
    print(key," - " ,value)

# Correr la lista
for element in super_list:
    print(element)

if __name__ == '__main__':
    run()