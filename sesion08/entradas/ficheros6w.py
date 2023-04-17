import pprint as pp
def main():
    f = open("miFichero.txt", "w")
    f.write("Hola Mundo")
    f.write("\ndatos2")
    f.close()


if __name__ == "__main__":
    main()

