# /*
#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
#  */

def run():
    
    def equilibra_expresion(expresion):
        
        if (expresion.count("{")) == (expresion.count("}")) and (expresion.count("(")) == (expresion.count(")")) and (expresion.count("[")) == (expresion.count("]")):
            print("Expresion balanceada")
        else:
            print("Expresion no balanceada")

    equilibra_expresion("{ [ a * ( c + d ) ] - 5 }")
    equilibra_expresion("{ a * ( c + d ) ] - 5 }")

if __name__=="__main__":
    run()