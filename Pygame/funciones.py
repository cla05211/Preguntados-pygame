from datos import *
from constantes import *
import pygame

def crear_sublistas_lista(lista_elegida:list,valor_buscado:str)-> list:
    lista_final = []
    for diccionario in lista_elegida:
        lista_final.append(diccionario[valor_buscado])
    return lista_final

def determinar_si_respondio_bien(posicion_lista_preguntas:int,respuesta_elegida:str)-> bool:
    respondio_bien = False
    respuesta_correcta = lista_[posicion_lista_preguntas]["correcta"]

    if respuesta_elegida == respuesta_correcta:
        respondio_bien = True

    return respondio_bien

def  determinar_color_imagen_recuadro (lista_correctas:list,posicion_lista_preguntas:int,respuesta_elegida:str)-> str:
    respuesta_correcta = lista_correctas[posicion_lista_preguntas]
    if respuesta_elegida == "" or respuesta_elegida == respuesta_correcta:
        imagen = ruta_imagen_recuadro_respuesta
    elif respuesta_elegida != respuesta_correcta:
        imagen = ruta_imagen_recuadro_respuesta_roja
    return imagen

def dividir_string_en_dos_lineas (lista_strings:list,posicion_lista:int,linea_buscada:str)->str:
    pregunta = lista_strings[posicion_lista]
    largo_pregunta = len(pregunta)
    pregunta_largo_par = convertir_pregunta_impar_a_par(largo_pregunta)
    lista_palabras_pregunta = (pregunta.split(" "))
    linea_uno = ""
    linea_dos = ""
    i = 0
    for palabra in lista_palabras_pregunta:
        if i < (len(lista_palabras_pregunta)/2):
            linea_uno += palabra
            linea_uno += " "
            i += 1
        else:
            linea_dos += palabra
            linea_dos += " "
    if linea_buscada == "primera":
        return linea_uno
    else:
        return linea_dos

def determinar_si_cortar_string (ancho_pregunta:float,ancho_maximo:int)-> float:
    hay_que_cortar = False
    if ancho_pregunta > ancho_maximo:
        hay_que_cortar = True
    return hay_que_cortar

def cortar_texto(pantalla,lista_strings:list,posicion_listas:int,fuente_texto):
        primer_linea = dividir_string_en_dos_lineas(lista_strings,posicion_listas,"primera")
        segunda_linea = dividir_string_en_dos_lineas(lista_strings,posicion_listas,"segunda")
        texto_pregunta_linea_uno = fuente_texto.render(primer_linea,True,(COLOR_AMARILLO))
        texto_pregunta_linea_dos = fuente_texto.render(segunda_linea,True,(COLOR_AMARILLO))       
        pantalla.blit(texto_pregunta_linea_uno,(60,105))
        pantalla.blit(texto_pregunta_linea_dos,(60,150))

def determinar_si_numero_es_par(numero:int):
    es_par = False
    resto = numero % 2
    if resto == 0:
        es_par = True
    return es_par

def convertir_pregunta_impar_a_par(largo_pregunta:int) -> int:
    pregunta_es_par = determinar_si_numero_es_par(largo_pregunta)
    if not pregunta_es_par:
                largo_pregunta += 1
    return(largo_pregunta)

def cambiar_imagen_vidas_segun_intentos (intentos:int) -> str:
    match intentos:
        case 0:
            imagen = ruta_imagen_cero_vidas
        case 2:
            imagen = ruta_imagen_dos_vidas
        case 1:
            imagen = ruta_imagen_una_vida
    return imagen
    
def sacar_maximo_lista (lista_elegida:list)-> int :
    for i in range (0,len(lista_elegida),1):
            numero = lista_elegida[i]
            if i == 0 or maximo < numero:
                maximo = numero
    return maximo                
