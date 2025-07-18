from gramatica import generar_gramatica_enumerada

def main():
    try:
        n = int(input("Ingrese un número entero n (≥ 0): "))
        if n < 0:
            print("El número debe ser mayor o igual a 0.")
            return

        gramatica = generar_gramatica_enumerada(n)

        print(f"\nGramática número {gramatica['n']}:")
        print(f"- Variables usadas ({gramatica['VariablesUsadas']}): {gramatica['Variables']}")
        print(f"- Terminales: {gramatica['Terminales']}")
        print(f"- Símbolo inicial: {gramatica['Inicial']}")
        print(f"- Total de reglas posibles: {gramatica['TotalReglas']}")
        print("\nProducciones seleccionadas:")
        for i, regla in enumerate(gramatica['Producciones'], start=1):
            print(f"  {i}. {regla}")

    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")

if __name__ == "__main__":
    main()
