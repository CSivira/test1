from Memory import Memory


def main():
    memory = Memory(1024)

    memory.reserve(32, 'A')
    memory.free('A')
    # memory.reserve(64, 'B')
    # memory.reserve(60, 'C')
    # memory.reserve(150, 'D')
    # memory.free('B')
    # memory.free('A')
    # memory.reserve(100, 'E')

    memory.show()

    """ while True:
        action = input("Introduce una acción: ")
        if action == "reserve":
            amount = int(input("Introduce la amount de bloques a reserve: "))
            name = input("Introduce el name del bloque: ")
            memory.reserve(amount, name)
        elif action == "free":
            name = input("Introduce el name del bloque a free: ")
            memory.free(name)
        elif action == "show":
            memory.show()
        elif action == "SALIR":
            break """


if __name__ == "__main__":
    main()
