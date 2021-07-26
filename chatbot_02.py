# silenciar mensajes de advertencia
import warnings
warnings.filterwarnings("ignore")

''' importamos los clasificadores'''
from clasificadores import *
import os
while True:
    try:
        # Acá tiene que ir toda la lógica del Chatbot
        
        # Le pedimos que ingrese su consulta
        os.system('cls')
        print('Hola soy Timon, un asistente virtual ;).¿En que puedo ayudarte?\n')
        oracion_input=input("Ingrese su consulta: ")
        
        '''
        Pasaremos la oracion_input a los distintos clasificadores y elaboraremos
        una respuesta.
        
        Tarea: 
            Crear el clasificador_intenciones(oracion_input) 
            Sugerimos usar un modelo que también nos devuelva la probabilidad
            Debería devolver la intención y la probabilidad
            
            - Hemos creado el clasificador_intenciones que 
            nos devuelve la intención y la probabilidad.
            
            -También tenemos que  crear el clasificador_carreras(oracion_input)
            que nos devuelva la carrera y la probabilidad.
            
            - Idem para el clasificador_subIntencion(oracion_input)
            - Idem para el clasificador_w5(oracion_input)           
        '''
        
        # CLASIFICADOR DE INTENCIONES: 
        
        intencion, prob_intencion = clasificador_intenciones(oracion_input)
        
        ''' el print siguiente es sólo PARA VISUALIZAR LA INTENCIÓN Y LA 
            PROBABILIDAD DE LA MISMA LUEGO DE PROBAR, QUITAR
        '''
        print('Intencion =', intencion, prob_intencion)

        if intencion == 'pagos':      
            # CLASIFICADOR DE SUBINTENCIONES PAGOS: 
            
            subintencion, prob_intencion = clasificador_subintenciones_pago(oracion_input)
            
        
            #print('SubIntencion', subintencion_pago, prob_intencion)

        elif intencion == 'tramite':
            # CLASIFICADOR DE SUBINTENCIONES TRAMITES: 
            
            subintencion, prob_intencion = clasificador_subintenciones_tramite(oracion_input)
            
        else:
            subintencion,prob_intencion=('todas',1)
        
        print('SubIntencion=', subintencion, prob_intencion)

        # if subintencion != 'todas':
        # CLASIFICADOR DE CARRERAS
        carrera, prob_intencion = clasificador_carreras(oracion_input)
        
        ''' el print siguiente es sólo PARA VISUALIZAR LA INTENCIÓN Y LA 
            PROBABILIDAD DE LA MISMA LUEGO DE PROBAR, QUITAR
        '''
        #if carrera != "todas":
        print('Carrera =', carrera, prob_intencion)

        # CLASIFICADOR DE W5
        intencion_w5, prob_intencion = clasificador_w5(oracion_input)
        
        ''' el print siguiente es sólo PARA VISUALIZAR LA INTENCIÓN Y LA 
            PROBABILIDAD DE LA MISMA LUEGO DE PROBAR, QUITAR
        '''
        print('W5 =', intencion_w5, prob_intencion)
        
        # OTROS CLASIFICADORES
        
        '''
            Generar una respuesta en función de los clasificadores obtenidos
            accediendo a la base de datos respuestas
        ''' 
        import pymongo
        client = pymongo.MongoClient(
        "mongodb+srv://federico:uUmQB7B1sF5ytXg8@cluster0.ix9a2.mongodb.net/chatbot?retryWrites=true&w=majority")
        db = client.chatbot

        intencion_r= intencion
        subintencion_r = subintencion
        carrera_r = carrera
        w5 = intencion_w5

        Documento = db.respuestas.find_one({"intencion": intencion_r, "subintencion": subintencion_r, "carrera": carrera_r, "w5": intencion_w5})
        
        
        #respuesta = "Aquí iria la respuesta del chatbot"
        
        print("----------------------------------------------")
        print("Timon dice: ")
        if Documento:
            print(Documento['respuesta'])
        else:
            print('Disculpe no puedo responder esa pregunta')

        print("----------------------------------------------")
        
        # Después de cada respuesta le preguntamos al usuario si quiere continuar.
        
        desea_continuar=input("Desea continuar? Ingrese s o n: ").lower()
        if (desea_continuar=="n"):
            # Nos despedimos
            
            print("----------------------------------------------")
            print("Timon dice: ")
            print("Chau, hasta la próxima!")
            print("----------------------------------------------")
            
            # y cortamos el while para terminar 
            break
        
    except (KeyboardInterrupt, EOFError, SystemExit):
        break