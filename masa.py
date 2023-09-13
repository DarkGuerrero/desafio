def kg_gramos (Kilogramos):
    return Kilogramos * 1000

def kg_toneladas (Kilogramos):
    return Kilogramos / 1000

def toneladas_gramos (toneladas):
    return toneladas * 1000

if __name__=="__main__":
    Kilogramos =2.5
    gramos = kg_gramos(Kilogramos)
    print(f"{Kilogramos} kg son equivalente a {gramos} g ")