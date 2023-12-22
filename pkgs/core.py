#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import os
import unidecode


# seminars {{{
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
        "talk": r"A formula of Simons' type and hypersurfaces with constant mean curvature",
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
        "talk": r"Static perfect fluid space and closed minimal hypersufaces",
        "date": {
            "dd": r"1",
            "mm": r"agosto",
            "yy": r"2023",
        },
        "addr": r"",
    },
    16: {
        "name": r"Miriam Cristina",
        "talk": r"Fluxo Redutor de Curvas",
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
# }}}


# set_metadata {{{
def set_metadata(name, talk, day, month, year):
    cmd = r"\seminar{%s}{%s}{%s}{%s}{%s}" % (name, talk, day, month, year)
    with open("auth.tex", "w") as f:
        print(cmd, file=f)


# }}}


# generate_pdf {{{
def generate_pdf(name, talk, date, addr):
    os.system("xelatex main; xelatex main")
    renaming = "pdf/cert_{}_{}_{}_{}.pdf".format(
        unidecode.unidecode(name).lower().replace(" ", "_"),
        date["dd"],
        date["mm"],
        date["yy"],
    )
    os.system(r"mv main.pdf {}".format(renaming))
    return renaming


# }}}


# sendmail {{{
def sendmail(name, talk, day, month, year, addr, cert):
    body = r"""
    Olá, {}!

    Eis aqui o certificado do seu seminário de geometria, intitulado

      {},

    o qual foi ministrado em {} de {} de {}.

    Agradecemos imensamente pela participação.

    Atenciosamente,
    Marcelo Bezerra
    """.format(
        name, talk, day, month, year
    )
    with open("mail.txt", "w") as f:
        print(body, file=f)
    subject = r"certificado de apresentação do seu seminário de geometria"
    muttcmd = r"mutt -s '{}' -a {} -- {} < mail.txt".format(
        subject, cert, addr
    )
    os.system(muttcmd)


# }}}


def main():
    # for k in seminar.keys():
    for k in [3]:
        if seminar[k]["talk"]:
            name = seminar[k]["name"]
            talk = seminar[k]["talk"]
            date = seminar[k]["date"]
            addr = seminar[k]["addr"]
            set_metadata(name, talk, date["dd"], date["mm"], date["yy"])
            cert = generate_pdf(name, talk, date, addr)
            sendmail(
                name, talk, date["dd"], date["mm"], date["yy"], addr, cert
            )


if __name__ == "__main__":
    main()
