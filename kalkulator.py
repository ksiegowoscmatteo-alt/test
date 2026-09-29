"""Prosty kalkulator dodawania."""


def dodaj(a, b):
    return a + b


def main():
    print("Kalkulator dodawania")
    try:
        a = float(input("Podaj pierwszą liczbę: ").replace(",", "."))
        b = float(input("Podaj drugą liczbę: ").replace(",", "."))
    except ValueError:
        print("To nie jest poprawna liczba.")
        return
    print(f"Wynik: {a} + {b} = {dodaj(a, b)}")


if __name__ == "__main__":
    main()
