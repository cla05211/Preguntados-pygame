import pygame
from constantes import *
from datos import *
from funciones import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(VOLUMEN_SONIDOS)

pantalla = pygame.display.set_mode([ANCHO_VENTANA,ALTO_VENTANA])
corriendo = True
score = 0
posicion_listas = 0
intentos = 2
respondio_bien = False
toco_respuesta = False
cambiar_color_recuadros = False
completo_partida = False
lista_score = []
lista_preguntas = crear_sublistas_lista(lista_,"pregunta")
lista_respuestas_a = crear_sublistas_lista(lista_,"a")
lista_respuestas_b = crear_sublistas_lista(lista_,"b")
lista_respuestas_c = crear_sublistas_lista(lista_,"c")
lista_respuestas_correctas = crear_sublistas_lista(lista_,"correcta")
#Sonidos
sonido_inicio = pygame.mixer.Sound(RUTA_SONIDO_INICIO)
sonido_incorrecto = pygame.mixer.Sound(RUTA_SONIDO_INCORRECTO)
sonido_correcto = pygame.mixer.Sound(RUTA_SONIDO_CORRECTO)
sonido_inicio.play()
#Imagenes
imagen_recuadros_pregunta_score = pygame.image.load(ruta_imagen_recuadros)
imagen_corazones_actual = cambiar_imagen_vidas_segun_intentos(intentos)
imagen_corazones = pygame.image.load(imagen_corazones_actual)
imagen_personaje = pygame.image.load(ruta_imagen_willy)
imagen_correcto = pygame.image.load(ruta_imagen_correcto)
imagen_incorrecto = pygame.image.load(ruta_imagen_incorrecto)
imagen_partida_terminada = pygame.image.load(ruta_imagen_reiniciar)
#Textos 
FUENTE_TITULO = pygame.font.SysFont(FUENTE_FINA,TAMAÑO_FUENTE_TITULO)
FUENTE_TEXTO = pygame.font.SysFont(FUENTE_GRUESA,TAMAÑO_FUENTE_TEXTO)
FUENTE_SCORE = pygame.font.SysFont(FUENTE_FINA,TAMAÑO_FUENTE_SCORE)
titulo_pregunta = FUENTE_TITULO.render(str("SIGUIENTE PREGUNTA"),True,(COLOR_AMARILLO))
texto_reiniciar = FUENTE_TITULO.render(str("R E I N I C I A R"),True,(COLOR_AMARILLO))


while corriendo:
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                corriendo = False

    pygame.display.set_caption("Preguntados") #Titulo ventana
    pantalla.fill((COLOR_GRIS))

    #Recuadros
    pygame.draw.rect (pantalla,COLOR_TURQUESA,(0,0,1000,70))
    pygame.draw.rect (pantalla,COLOR_TURQUESA,(0,530,1000,70))
    pygame.draw.rect (pantalla,COLOR_TURQUESA_OSCURO,(195,0,650,70))
    pygame.draw.rect (pantalla,COLOR_TURQUESA_OSCURO,(285,530,395,70))
        
    if completo_partida == False:
        if  cambiar_color_recuadros == False:
            color_recuadro_a = determinar_color_imagen_recuadro(lista_respuestas_correctas,posicion_listas,"")
            color_recuadro_b = determinar_color_imagen_recuadro(lista_respuestas_correctas,posicion_listas,"")
            color_recuadro_c = determinar_color_imagen_recuadro(lista_respuestas_correctas,posicion_listas,"")

        #Textos        
        texto_pregunta = FUENTE_TEXTO.render((lista_preguntas[posicion_listas]),True,(COLOR_AMARILLO))
        texto_respuesta_a = FUENTE_TEXTO.render((lista_respuestas_a[posicion_listas]),True,(COLOR_AMARILLO))
        texto_respuesta_b = FUENTE_TEXTO.render((lista_respuestas_b[posicion_listas]),True,(COLOR_AMARILLO))
        texto_respuesta_c = FUENTE_TEXTO.render((lista_respuestas_c[posicion_listas]),True,(COLOR_AMARILLO))
        texto_score = FUENTE_SCORE.render(str(score),True,(COLOR_AMARILLO))

        #CLICK
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
        #Reiniciar
                if (posicion_click[0] > 285 and posicion_click[0] < 680) and (posicion_click[1] > 530 and posicion_click[1] < 600):
                    score = 0
                    posicion_listas = 0
                    intentos = 2
                    respondio_bien = False
                    toco_respuesta = False
                    cambiar_color_recuadros = False
                #Pregunta
                elif (posicion_click[0] > 195 and posicion_click[0] < 845) and (posicion_click[1] > 1 and posicion_click[1] < 70):
                    if posicion_listas == (len(lista_preguntas)-1):
                        completo_partida = True
                        continue
                    intentos = 2
                    respondio_bien = False
                    posicion_listas += 1
                    toco_respuesta = False
                    cambiar_color_recuadros = False

                if intentos != 0 and not respondio_bien:
                    if (posicion_click[0] > 40 and posicion_click[0] < 440) and (posicion_click[1] > 240 and posicion_click[1] < 310):
                        respuesta_elegida = "a"
                        color_recuadro_a = determinar_color_imagen_recuadro(lista_respuestas_correctas,posicion_listas,"a")
                        cambiar_color_recuadros = True
                        toco_respuesta = True
                    elif (posicion_click[0] > 40 and posicion_click[0] < 440) and (posicion_click[1] > 335 and posicion_click[1] < 405):
                        respuesta_elegida = "b"
                        color_recuadro_b = determinar_color_imagen_recuadro(lista_respuestas_correctas,posicion_listas,"b")
                        cambiar_color_recuadros = True
                        toco_respuesta = True
                    elif (posicion_click[0] > 40 and posicion_click[0] < 440) and (posicion_click[1] > 430 and posicion_click[1] < 503):
                        respuesta_elegida = "c"
                        color_recuadro_c = determinar_color_imagen_recuadro(lista_respuestas_correctas,posicion_listas,"c")
                        cambiar_color_recuadros = True
                        toco_respuesta = True
        if toco_respuesta:
            respondio_bien = determinar_si_respondio_bien(posicion_listas,respuesta_elegida)
            cambiar_color_recuadros = True
            if respondio_bien:
                score += 10
                sonido_correcto.play()
                toco_respuesta = False
            else: 
                intentos -= 1
                sonido_incorrecto.play()
                toco_respuesta = False

        imagen_recuadro_a = pygame.image.load(color_recuadro_a)
        imagen_recuadro_b = pygame.image.load(color_recuadro_b)
        imagen_recuadro_c = pygame.image.load(color_recuadro_c)

        pantalla.blit(imagen_recuadro_a,(0,0))
        pantalla.blit(imagen_recuadro_b,(0,98))
        pantalla.blit(imagen_recuadro_c,(0,196))
        pantalla.blit(titulo_pregunta,(200,-5))
        pantalla.blit(imagen_recuadros_pregunta_score,(0,0))
        pantalla.blit(imagen_corazones,(20,533))
        pantalla.blit(texto_respuesta_a,(70,245))
        pantalla.blit(texto_respuesta_b,(70,345))
        pantalla.blit(texto_respuesta_c,(70,440))
        pantalla.blit(texto_reiniciar,(295,525))
        pantalla.blit(texto_score,(842,105))

        #Pregunta
        ancho_texto_pregunta = texto_pregunta.get_width()
        hay_que_cortar_texto_pregunta = determinar_si_cortar_string(ancho_texto_pregunta,600)
        if hay_que_cortar_texto_pregunta:
            cortar_texto(pantalla,lista_preguntas,posicion_listas,FUENTE_TEXTO)
        else:
            pantalla.blit(texto_pregunta,(60,125))

        if respondio_bien:
            pantalla.blit(imagen_correcto,(0,0))
        elif intentos == 0:
            pantalla.blit(imagen_incorrecto,(0,0))
        else: 
            pantalla.blit(imagen_personaje,(20,12))

    if completo_partida:
        lista_score.append(score)
        score_maximo = sacar_maximo_lista(lista_score)
        texto_score_partida = FUENTE_TITULO.render(str(score),True,(COLOR_AMARILLO))
        texto_score_maximo = FUENTE_TITULO.render(str(score_maximo),True,(COLOR_AMARILLO))
        pantalla.blit(imagen_partida_terminada,(0,0))
        pantalla.blit(texto_score_partida,(560,286))
        pantalla.blit(texto_score_maximo,(710,363))
        pantalla.blit(texto_reiniciar,(295,525))

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_click = list(evento.pos)
        #Reiniciar
                if (posicion_click[0] > 285 and posicion_click[0] < 680) and (posicion_click[1] > 530 and posicion_click[1] < 600):
                    score = 0
                    posicion_listas = 0
                    intentos = 2
                    respondio_bien = False
                    toco_respuesta = False
                    cambiar_color_recuadros = False
                    completo_partida = False
                    sonido_inicio.play()
        
    pygame.display.flip() 

pygame.quit()