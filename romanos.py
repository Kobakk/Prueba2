class Solucion:
    def RomanosAEnteros(self, a: str) -> int:
        romanos = {
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000
                }
        
        resultado = 0
        preresultado = 0

        for x in reversed(a):
            if romanos[x] >= preresultado:
                resultado += romanos[x]

            else:
                resultado -= romanos[x]

            preresultado = resultado[x]

        return resultado

print(Solucion())
