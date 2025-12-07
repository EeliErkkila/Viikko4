"""
Ohjelma joka tulostaa tiedostosta luettujen varausten alkiot ja niiden tietotyypit

varausId | nimi | sähköposti | puhelin | varauksenPvm | varauksenKlo | varauksenKesto | hinta | varausVahvistettu | varattuTila | varausLuotu
------------------------------------------------------------------------
201 | Muumi Muumilaakso | muumi@valkoinenlaakso.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Metsätila 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
202 | Niiskuneiti Muumilaakso | niisku@muumiglam.fi | 0451122334 | 2025-12-01 | 11:30:00 | 1 | 12.00 | False | Kukkahuone | 2025-09-03 09:12:48
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
203 | Pikku Myy Myrsky | myy@pikkuraivo.net | 0415566778 | 2025-10-22 | 15:45:00 | 3 | 27.90 | True | Punainen Huone | 2025-07-29 18:05:11
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
204 | Nipsu Rahapulainen | nipsu@rahahuolet.me | 0442233445 | 2025-09-18 | 13:00:00 | 4 | 39.95 | False | Varastotila N | 2025-08-01 10:59:02
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
205 | Hemuli Kasvikerääjä | hemuli@kasvikeraily.club | 0463344556 | 2025-11-05 | 08:15:00 | 2 | 19.95 | True | Kasvitutkimuslabra | 2025-10-09 16:41:55
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
"""
from datetime import datetime
# Tässä tiedostossa määritellään funktioita varaustietojen lukemiseen ja muuntamiseen
def muunna_varaustiedot(rivi: list) -> list:

    jono = [item.strip() for item in rivi]

    varaus_id = int(jono[0])

    nimi = jono[1]

    sahkoposti = jono[2]

    puhelin = jono[3]

    varauksen_pvm = datetime.strptime(jono[4], "%Y-%m-%d").date()

    varauksen_klo = datetime.strptime(jono[5], "%H:%M").time()

    varauksen_kesto = int(jono[6])

    hinta = float(jono[7])

    varaus_vahvistettu = (jono[8] == "True")

    varattu_tila = jono[9]

    varaus_luotu = datetime.strptime(jono[10], "%Y-%m-%d %H:%M:%S")

    return [
        varaus_id, nimi, sahkoposti, puhelin,
        varauksen_pvm, varauksen_klo,
        varauksen_kesto, hinta,
        varaus_vahvistettu, varattu_tila,
        varaus_luotu
    ]

def hae_varaukset(varaustiedosto: str) -> list:
    # HUOM! Tälle funktioille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

# Pääohjelma
def main():
    varausdata = hae_varaukset("varaukset.txt")
    # Tulostetaan varaukset eri kriteereillä
    print("1) Vahvistetut varaukset")
    for merkinta in varausdata[1:]:
        if merkinta[8] == True:
            print(f'- {merkinta[1]}, {merkinta[9]}, {merkinta[4].strftime("%d.%m.%Y")}, klo {merkinta[5].strftime("%H.%M")}')
    print()
    # Tulostetaan pitkät varaukset
    print("2) Pitkät varaukset (> 3 h)")
    for merkinta in varausdata[1:]:
        if merkinta[6] >= 3:
            print(
                f'- {merkinta[1]}, {merkinta[4].strftime("%d.%m.%Y")} klo {merkinta[5].strftime("%H.%M")}'
                f' kesto {merkinta[6]} h, {merkinta[9]}'
            )
    print()
    # Tulostetaan varauksen vahvistusstatus
    print("3) Varausten vahvistusstatus")
    for merkinta in varausdata[1:]:
        if merkinta[8]:
            print(f'{merkinta[1]} -> Vahvistettu')
        else:
            print(f'{merkinta[1]} -> Ei vahvistettu')
    print()
    # Tulostetaan yhteenveto vahvistuksista
    print("4) Yhteenveto Vahvistuksista")
    tunnistetut = 0
    tunnistamattomat = 0

    for merkinta in varausdata[1:]:
        if merkinta[8]:
            tunnistetut += 1
        else:
            tunnistamattomat += 1

    print(f'- Vahvistettuja varauksia: {tunnistetut} kpl')
    print(f'- Ei-vahvistettuja varauksia: {tunnistamattomat} kpl')
    print()
    # Tulostetaan vahvistettujen varausten kokonaistulot
    print("5) Vahvistettujen varausten kokonaistulot")
    summa_rahana = 0

    for merkinta in varausdata[1:]:
        if merkinta[8]:
            yksikkohinta = merkinta[7]
            tunnit = merkinta[6]
            summa_rahana += yksikkohinta * tunnit

    print(f'Vahvistettujen varausten kokonaistulot: {summa_rahana} €')

if __name__ == "__main__":
    main()
