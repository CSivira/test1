def main():
    programs = {}
    interpreters = {}
    translators = {}

    def show():
        print("-------------------------------------------------------------")
        for name, language in programs.items():
            print(f"  PROGRAMA {name} {language}")
        for language, base in interpreters.items():
            print(f"  INTERPRETE {language} {base}")
        for base, rest in translators.items():
            for origin, destiny in rest.items():
                print(f"  TRADUCTOR {base} {origin} {destiny}")
        print("-------------------------------------------------------------")

    def is_compilable(language):
        if language == "LOCAL":
            return True

        if language in interpreters and is_compilable(interpreters[language]):
            return True

        for base in translators:
            if language in translators[base] and is_compilable(base):
                return True

        return False

    while True:
        command = input()

        if len(command) == 0 or command is None:
            print("~")
            continue

        command = command.split(" ")
        if command[0] == "DEFINIR":
            if len(command) == 4 and command[1] == "PROGRAMA":
                programs[command[2]] = command[3]
                print(f"Se definió el programa '{command[2]}', ejecutable en '{command[3]}'")
            elif len(command) == 4 and command[1] == "INTERPRETE":
                interpreters[command[3]] = command[2]
                print(f"Se definió un intérprete para '{command[3]}', escrito en '{command[2]}'")
            elif len(command) == 5 and command[1] == "TRADUCTOR":
                if command[3] not in translators:
                    translators[command[2]] = {}
                translators[command[2]][command[3]] = command[4]
                print(f"Se definió un traductor de '{command[3]}' hacia '{command[4]}', escrito en '{command[2]}'")
            else:
                print("Comando desconocido")
        elif command[0] == "EJECUTABLE":
            # show()
            if len(command) != 2 or command[1] not in programs:
                print(f"No existe un programa con el name '{command[1]}'")
            elif is_compilable(programs[command[1]]):
                print(f"Si, es posible ejecutar el programa '{command[1]}'")
            else:
                print(f"No es posible ejecutar el programa '{command[1]}'")
        elif command[0] == "SALIR":
            break
        else:
            print("Comando desconocido")


if __name__ == "__main__":
    main()
