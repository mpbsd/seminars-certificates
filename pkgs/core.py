#!/usr/bin/env python3


import os
import unidecode


seminar = {
    0: {
        "name": r"Ilton Menezes",
        "talk": r"Rigidity results on $\rho$-Einstein solitons with zero scalar curvature",
        "date": {
            "dd": r"18",
            "mm": r"abril",
            "yy": r"2023",
        },
    },
    1: {
        "name": r"Willian Isao Tokura",
        "talk": r"Yamabe solitons imersos em formas espaciais",
        "date": {
            "dd": r"25",
            "mm": r"abril",
            "yy": r"2023",
        },
    },
    2: {
        "name": r"Alejandra Munoz",
        "talk": r"Classificação de superfícies separáveis com curvatura Gaussiana constante",
        "date": {
            "dd": r"2",
            "mm": r"maio",
            "yy": r"2023",
        },
    },
    3: {
        "name": r"Marcelo Bezerra Barboza",
        "talk": r"A formula of Simons' type and hypersurface with constant mean curvature",
        "date": {
            "dd": r"9",
            "mm": r"maio",
            "yy": r"2023",
        },
    },
    4: {
        "name": r"Armando Vasquez Corro",
        "talk": r"Ribaucour surfaces of harmonic type",
        "date": {
            "dd": r"16",
            "mm": r"maio",
            "yy": r"2023",
        },
    },
    5: {
        "name": r"Hudson Pina",
        "talk": r"Gap theorems for minimal submanifolds of a hyperbolic space",
        "date": {
            "dd": r"23",
            "mm": r"maio",
            "yy": r"2023",
        },
    },
    6: {
        "name": r"Douglas Hilário",
        "talk": r"Geometria dos tecidos",
        "date": {
            "dd": r"30",
            "mm": r"maio",
            "yy": r"2023",
        },
    },
    7: {
        "name": r"Ronaldo Garcia",
        "talk": r"Problema do transporte, imagens e linhas de curvatura",
        "date": {
            "dd": r"6",
            "mm": r"junho",
            "yy": r"2023",
        },
    },
    8: {
        "name": r"Adriano Cavalcante",
        "talk": r"Umbilicity of constant mean curvature hypersurfaces into space forms",
        "date": {
            "dd": r"13",
            "mm": r"junho",
            "yy": r"2023",
        },
    },
    9: {
        "name": r"Fabio Nunes",
        "talk": r"Self-similar solutions to the curvature flow and its inverse on the $2$-dimensional light cone",
        "date": {
            "dd": r"20",
            "mm": r"junho",
            "yy": r"2023",
        },
    },
    10: {
        "name": r"Hiuri Fellipe",
        "talk": r"Soluções auto similares do fluxo redutor de curvas na esfera",
        "date": {
            "dd": r"27",
            "mm": r"junho",
            "yy": r"2023",
        },
    },
    11: {
        "name": r"Adriana Araújo Cintra",
        "talk": r"Fórmula de Liouville e as superfícies mínimas no espaço de Lorentz-Minkowski tridimensional",
        "date": {
            "dd": r"4",
            "mm": r"julho",
            "yy": r"2023",
        },
    },
    12: {
        "name": r"Valter Borges",
        "talk": r"",
        "date": {
            "dd": r"11",
            "mm": r"julho",
            "yy": r"2023",
        },
    },
    13: {
        "name": r"Raquel Pereira de Araújo",
        "talk": r"Novas classes de superfícies de Weingarten generalizadas",
        "date": {
            "dd": r"18",
            "mm": r"julho",
            "yy": r"2023",
        },
    },
    14: {
        "name": r"",
        "talk": r"",
        "date": {
            "dd": r"25",
            "mm": r"julho",
            "yy": r"2023",
        },
    },
    15: {
        "name": r"Thamara Policarpo",
        "talk": r"",
        "date": {
            "dd": r"1",
            "mm": r"agosto",
            "yy": r"2023",
        },
    },
    16: {
        "name": r"Miriam Cristina",
        "talk": r"",
        "date": {
            "dd": r"8",
            "mm": r"agosto",
            "yy": r"2023",
        },
    },
    17: {
        "name": r"Alejandra Munoz",
        "talk": r"",
        "date": {
            "dd": r"15",
            "mm": r"agosto",
            "yy": r"2023",
        },
    },
    18: {
        "name": r"Guilherme Paes",
        "talk": r"",
        "date": {
            "dd": r"22",
            "mm": r"agosto",
            "yy": r"2023",
        },
    },
}


def seminarcmd(name, talk, day, month, year):
    latexcmd = r"\seminar{%s}{%s}{%s}{%s}{%s}" % (name, talk, day, month, year)
    return latexcmd


def main():
    # for k in seminar.keys():
    for k in [1, 3]:
        if seminar[k]["talk"]:
            name = seminar[k]["name"]
            talk = seminar[k]["talk"]
            date = seminar[k]["date"]
            cert = "pdf/cert_{}_{}_{}_{}.pdf".format(
                unidecode.unidecode(name).lower().replace(" ", "_"),
                date["dd"],
                date["mm"],
                date["yy"],
            )
            with open("auth.tex", "w") as f:
                print(
                    seminarcmd(name, talk, date["dd"], date["mm"], date["yy"]),
                    file=f,
                )
            os.system("xelatex main")
            os.system("xelatex main")
            os.system("mv main.pdf {}".format(cert))


if __name__ == "__main__":
    main()
