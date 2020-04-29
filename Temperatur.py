def um(C = 0):
    while True:
        C = input("Gib die Temperatur in Grad Celsius: ")
        try:
            C = float(C)
            return C
        except ValueError:
            print("Error:001")

def re(C):
      K = C + 273.15
      return K

if __name__ == "__main__":
    C = um
    print(um(re(C)))