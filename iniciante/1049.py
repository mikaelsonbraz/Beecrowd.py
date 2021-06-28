ent1 = input()
ent2 = input()
ent3 = input()
especies = [["vertebrado",
             ["ave",
              ["carnivoro", "aguia", "onivoro", "pombo"]],
             ["mamifero",
              ["onivoro", "homem", "herbivoro", "vaca"]]],
            ["invertebrado",
             ["inseto",
              ["hematofago", "pulga", "herbivoro", "lagarta"]],
             ["anelideo",
              ["hematofago", "sanguessuga", "onivoro", "minhoca"]]]]

especies2 = {"vertebrado": {"ave": {"carnivoro": "aguia", "onivoro": "pombo"}, "mamifero": {"onivoro": "homem", "herbivoro": "vaca"}},
            "invertebrado": {"inseto": {"hematofago": "pulga", "herbivoro": "lagarta"}, "analideo": {"hematofago": "sanguessuga", "onivoro": "minhoca"}}}


if especies[0][0] == ent1:
    if especies[0][1][0] == ent2:
        if especies[0][1][1][0] == ent3:
            print("aguia")
        elif especies[0][1][1][2] == ent3:
            print("pomba")
    elif especies[0][2][0] == ent2:
        if especies[0][2][1][0] == ent3:
            print("homem")
        elif especies[0][2][1][2] == ent3:
            print("vaca")
elif especies[1][0] == ent1:
    if especies[1][1][0] == ent2:
        if especies[1][1][1][0] == ent3:
            print("pulga")
        elif especies[1][1][1][2] == ent3:
            print("lagarta")
    elif especies[1][2][0] == ent2:
        if especies[1][2][1][0] == ent3:
            print("sanguessuga")
        elif especies[1][2][1][2] == ent3:
            print("minhoca")
