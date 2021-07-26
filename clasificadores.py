# silenciar mensajes de advertencia
import warnings
warnings.filterwarnings("ignore")


# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:36:30 2020

@author: AI
"""

def clasificador_intenciones(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro_filename = './ridge_intenciones.sav'
    logReg = pickle.load(open(cerebro_filename, 'rb'))
    vectorizer_filename='./vectorizer_intenciones.sav'
    vectorizador_intenciones = pickle.load(open(vectorizer_filename, 'rb'))

    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizador_intenciones.transform(oracion_input_array).toarray()
    intencion_pronosticada= logReg.predict(oracion_vectorizada)
    probabilidad= np.max(logReg.predict_proba(oracion_vectorizada))

    return intencion_pronosticada[0], probabilidad

def clasificador_subintenciones_pago(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro_filename = './ridge_subintenciones_pagos.sav'
    logReg = pickle.load(open(cerebro_filename, 'rb'))
    vectorizer_filename='./vectorizer_subintenciones_pagos.sav'
    vectorizador_intenciones = pickle.load(open(vectorizer_filename, 'rb'))
    
    
    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizador_intenciones.transform(oracion_input_array).toarray()
    intencion_pronosticada= logReg.predict(oracion_vectorizada)
    probabilidad= np.max(logReg.predict_proba(oracion_vectorizada))
    # if probabilidad >= 40:
    #     return intencion_pronosticada, probabilidad
    # else:
    #     print('Por favor sea mas especifico')
        
    return intencion_pronosticada[0], probabilidad

def clasificador_subintenciones_tramite(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro_filename = './ridge_subintenciones_tramite.sav'
    logReg = pickle.load(open(cerebro_filename, 'rb'))
    vectorizer_filename='./vectorizer_subintenciones_tramite.sav'
    vectorizador_intenciones = pickle.load(open(vectorizer_filename, 'rb'))
    
    
    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizador_intenciones.transform(oracion_input_array).toarray()
    intencion_pronosticada= logReg.predict(oracion_vectorizada)
    probabilidad= np.max(logReg.predict_proba(oracion_vectorizada))
    # if probabilidad >= 40:
    #     return intencion_pronosticada, probabilidad
    # else:
    #     print('Por favor sea mas especifico')
        
    return intencion_pronosticada[0], probabilidad

def clasificador_carreras(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro_filename = './ridge_carreras.sav'
    logReg = pickle.load(open(cerebro_filename, 'rb'))
    vectorizer_filename='./vectorizer_carreras.sav'
    vectorizador_intenciones = pickle.load(open(vectorizer_filename, 'rb'))
    
    
    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizador_intenciones.transform(oracion_input_array).toarray()
    intencion_pronosticada= logReg.predict(oracion_vectorizada)
    probabilidad= np.max(logReg.predict_proba(oracion_vectorizada))

    # if probabilidad >= 0.4:
    #     return intencion_pronosticada, probabilidad
   

    return intencion_pronosticada[0], probabilidad

def clasificador_w5(oracion_input):
    import pandas as pd
    import numpy as np
    import pickle
    import sklearn
    
    """
        Cargamos el archivo donde está guardado el cerebro_intenciones 
        y el vectorizador_intenciones con pickle
    """
    cerebro_filename = './ridge_w5.sav'
    logReg = pickle.load(open(cerebro_filename, 'rb'))
    vectorizer_filename='./vectorizer_w5.sav'
    vectorizador_intenciones = pickle.load(open(vectorizer_filename, 'rb'))
    
    
    
    '''
    Si había un preprocesamiento, efectuarlo aquí
    '''
    oracion_input_array=[oracion_input]  
        
    # La vectorizamos
    oracion_vectorizada=vectorizador_intenciones.transform(oracion_input_array).toarray()
    intencion_pronosticada= logReg.predict(oracion_vectorizada)
    probabilidad= np.max(logReg.predict_proba(oracion_vectorizada))

    return intencion_pronosticada[0], probabilidad
    
    # if probabilidad >= 0.4:
    #     return intencion_pronosticada, probabilidad
    # else:
    #     return probabilidad
        


'''
intencion, proba=clasificador_intenciones("Quiero saber cuánto cuesta la carrera de IA")

print(intencion, proba)
''' 