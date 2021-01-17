def recept(antal):
    print("\n")
    print("Ingredienser:")
    print("\n")
    print("Till formen:")
    print("- ca", antal*10/4, "g smör")
    print("- ca", antal*0.75/4, "dl ströbröd")
    print("\n")
    print("Sockerkaka:")
    print("-", int(antal*3/4), "st ägg")
    print("-", antal*3/4, "dl strösocker")
    print("-", antal*2/4, "tsk vaniljsocker")
    print("-", antal*2/4, "tsk bakpulver")
    print("-", antal*3/4, "dl vetemjöl")
    print("-", antal*75/4, "g smör")
    print("-", antal*1/4, "dl vatten")

def tidblanda(antal):
    return 10+antal

def tidgradda(antal):
    return 30+3*antal

def sockerkaka(antal):
    recept(antal)
    blandtid = tidblanda(antal)
    graddtid = tidgradda(antal)
    print("Tid för blandning:", blandtid, "minuter")
    print("Tid för gräddning:", graddtid, "minuter")

sockerkaka(4)
sockerkaka(7)
