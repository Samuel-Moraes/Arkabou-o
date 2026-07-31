import random

def calculoAtaqueFisico(soldadoUm, soldadoDois):

    # Soldado Um
    danoSoldadoUm = soldadoUm.getDano()

    # Soldado Dois
    vitalidadeSoldadoDois = soldadoDois.getVitalidade()
    resistenciaFisicaSoldadoDois = soldadoDois.getRf()
    esquivaSoldadoDois = soldadoDois.getEsquiva()
    esquivou = 1



    numeroSorteado = random.randint(0,100)
    if esquivaSoldadoDois <= numeroSorteado:
        esquivou = True
    else:
        esquivou = False
    
    danoCausado = (vitalidadeSoldadoDois - (danoSoldadoUm * resistenciaFisicaSoldadoDois) ) * esquivou
    return danoCausado

