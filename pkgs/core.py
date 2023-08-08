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
        "addr": r"",
    },
    1: {
        "name": r"Willian Isao Tokura",
        "talk": r"Yamabe solitons imersos em formas espaciais",
        "date": {
            "dd": r"25",
            "mm": r"abril",
            "yy": r"2023",
        },
        "addr": r"",
    },
    2: {
        "name": r"Alejandra Munoz",
        "talk": r"Classificação de superfícies separáveis com curvatura Gaussiana constante",
        "date": {
            "dd": r"2",
            "mm": r"maio",
            "yy": r"2023",
        },
        "addr": r"",
    },
    3: {
        "name": r"Marcelo Bezerra Barboza",
        "talk": r"A formula of Simons' type and hypersurface with constant mean curvature",
        "date": {
            "dd": r"9",
            "mm": r"maio",
            "yy": r"2023",
        },
        "addr": r"bezerra@ufg.br",
    },
    4: {
        "name": r"Armando Vasquez Corro",
        "talk": r"Ribaucour surfaces of harmonic type",
        "date": {
            "dd": r"16",
            "mm": r"maio",
            "yy": r"2023",
        },
        "addr": r"",
    },
    5: {
        "name": r"Hudson Pina",
        "talk": r"Gap theorems for minimal submanifolds of a hyperbolic space",
        "date": {
            "dd": r"23",
            "mm": r"maio",
            "yy": r"2023",
        },
        "addr": r"",
    },
    6: {
        "name": r"Douglas Hilário",
        "talk": r"Geometria dos tecidos",
        "date": {
            "dd": r"30",
            "mm": r"maio",
            "yy": r"2023",
        },
        "addr": r"",
    },
    7: {
        "name": r"Ronaldo Garcia",
        "talk": r"Problema do transporte, imagens e linhas de curvatura",
        "date": {
            "dd": r"6",
            "mm": r"junho",
            "yy": r"2023",
        },
        "addr": r"",
    },
    8: {
        "name": r"Adriano Cavalcante",
        "talk": r"Umbilicity of constant mean curvature hypersurfaces into space forms",
        "date": {
            "dd": r"13",
            "mm": r"junho",
            "yy": r"2023",
        },
        "addr": r"",
    },
    9: {
        "name": r"Fabio Nunes",
        "talk": r"Self-similar solutions to the curvature flow and its inverse on the $2$-dimensional light cone",
        "date": {
            "dd": r"20",
            "mm": r"junho",
            "yy": r"2023",
        },
        "addr": r"",
    },
    10: {
        "name": r"Hiuri Fellipe",
        "talk": r"Soluções auto similares do fluxo redutor de curvas na esfera",
        "date": {
            "dd": r"27",
            "mm": r"junho",
            "yy": r"2023",
        },
        "addr": r"",
    },
    11: {
        "name": r"Adriana Araújo Cintra",
        "talk": r"Fórmula de Liouville e as superfícies mínimas no espaço de Lorentz-Minkowski tridimensional",
        "date": {
            "dd": r"4",
            "mm": r"julho",
            "yy": r"2023",
        },
        "addr": r"",
    },
    12: {
        "name": r"Valter Borges",
        "talk": r"",
        "date": {
            "dd": r"11",
            "mm": r"julho",
            "yy": r"2023",
        },
        "addr": r"",
    },
    13: {
        "name": r"Raquel Pereira de Araújo",
        "talk": r"Novas classes de superfícies de Weingarten generalizadas",
        "date": {
            "dd": r"18",
            "mm": r"julho",
            "yy": r"2023",
        },
        "addr": r"",
    },
    14: {
        "name": r"",
        "talk": r"",
        "date": {
            "dd": r"25",
            "mm": r"julho",
            "yy": r"2023",
        },
        "addr": r"",
    },
    15: {
        "name": r"Thamara Policarpo",
        "talk": r"",
        "date": {
            "dd": r"1",
            "mm": r"agosto",
            "yy": r"2023",
        },
        "addr": r"",
    },
    16: {
        "name": r"Miriam Cristina",
        "talk": r"",
        "date": {
            "dd": r"8",
            "mm": r"agosto",
            "yy": r"2023",
        },
        "addr": r"",
    },
    17: {
        "name": r"Alejandra Munoz",
        "talk": r"",
        "date": {
            "dd": r"15",
            "mm": r"agosto",
            "yy": r"2023",
        },
        "addr": r"",
    },
    18: {
        "name": r"Guilherme Paes",
        "talk": r"",
        "date": {
            "dd": r"22",
            "mm": r"agosto",
            "yy": r"2023",
        },
        "addr": r"",
    },
}


def seminarcmd(name, talk, day, month, year):
    latexcmd = r"\seminar{%s}{%s}{%s}{%s}{%s}" % (name, talk, day, month, year)
    return latexcmd


def mailcmd(name, talk, day, month, year, addr, cert):
    body = r"""
    Olá, {}!

    Eis aqui o certificado do seu seminário intitulado

      {},

    ministrado no dia {} de {} de {}.

    Agradecemos imensamente pela participação.

    Atenciosamente,
    Marcelo Bezerra
    """.format(name, talk, day, month, year)
    with open("mail.txt", "w") as f:
        print(body, file=f)
    subject = r"certificado seminario de geometria"
    muttcmd = r"mutt -s '{}' -a {} -- {} < mail.txt"
    return muttcmd.format(subject, cert, addr)


def main():
    # for k in seminar.keys():
    for k in range(17):
        if seminar[k]["talk"]:
            name = seminar[k]["name"]
            talk = seminar[k]["talk"]
            date = seminar[k]["date"]
            addr = seminar[k]["addr"]
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
            # os.system(
            #     mailcmd(
            #         name, talk, date["dd"], date["mm"], date["yy"], addr, cert
            #     )
            # )


if __name__ == "__main__":
    main()
