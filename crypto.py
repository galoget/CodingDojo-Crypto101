#!/usr/bin/env python 

cadena = "¿A dónde voy?" 

desplazamiento = 3 

 

def encriptar (cadena, desplazamiento): 

    letras_mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 

                         "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 

                         "U", "V", "W", "X", "Y", "Z"] 

    letras_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 

                         "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 

                         "u", "v", "w", "x", "y", "z"] 

    letras_mayusculas_desplazadas = letras_mayusculas[desplazamiento:] + \ 

                                    letras_mayusculas[:desplazamiento] 

    letras_minusculas_desplazadas = letras_minusculas[desplazamiento:] + \ 

                                    letras_minusculas[:desplazamiento] 

    lista_caracteres = [] 

 

    for caracter in cadena: 

        if caracter in letras_mayusculas: 

            lista_caracteres.append(letras_mayusculas_desplazadas \ 

                                    [letras_mayusculas.index(caracter)]) 

        elif caracter in letras_minusculas: 

            lista_caracteres.append(letras_minusculas_desplazadas \ 

                                    [letras_minusculas.index(caracter)]) 

        else: 

            lista_caracteres.append(caracter) 

 

    nueva_cadena = "".join(lista_caracteres) 

 

    return nueva_cadena 

 

def desencriptar (cadena, desplazamiento): 

    letras_mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 

                         "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 

                         "U", "V", "W", "X", "Y", "Z"] 

    letras_minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 

                         "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 

                         "u", "v", "w", "x", "y", "z"] 

    letras_mayusculas_desplazadas = letras_mayusculas[-desplazamiento:] + \ 

                                    letras_mayusculas[:-desplazamiento] 

    letras_minusculas_desplazadas = letras_minusculas[-desplazamiento:] + \ 

                                    letras_minusculas[:-desplazamiento] 

    lista_caracteres = [] 

 

    for caracter in cadena: 

        if caracter in letras_mayusculas: 

            lista_caracteres.append(letras_mayusculas_desplazadas \ 

                                    [letras_mayusculas.index(caracter)]) 

        elif caracter in letras_minusculas: 

            lista_caracteres.append(letras_minusculas_desplazadas \ 

                                    [letras_minusculas.index(caracter)]) 

        else: 

            lista_caracteres.append(caracter) 

 

    nueva_cadena = "".join(lista_caracteres) 

 

    return nueva_cadena 
