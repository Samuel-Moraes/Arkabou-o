from heroClass import Hero
import movimentos

membroUm = Hero(
    vitalidade= 100,
    mana= 100,
    dano = 100,
    rf= 0.1,
    rm = 0.1,
    rv = 0.1,
    rs = 0.1,
    ra = 0.1,
    acerto= 100,
    tCrit= 10,
    rMana= 10,
    rVit= 10,
    iniciativa= 10,
    drein= 10,
    raca= 1,
    classe= 1,
    esquiva= 1
    )

membroDois = Hero(
    vitalidade= 100,
    mana= 100,
    dano = 100,
    rf= 0.1,
    rm = 0.1,
    rv = 0.1,
    rs = 0.1,
    ra = 0.1,
    acerto= 100,
    tCrit= 10,
    rMana= 10,
    rVit= 10,
    iniciativa= 10,
    drein= 10,
    raca= 1,
    classe= 1,
    esquiva= 99
    )

membroUm.printDosDados()

print(movimentos.calculoAtaqueFisico(membroUm, membroDois))

