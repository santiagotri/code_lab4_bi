# API - Laboratorio 4, inteligencia de negocios

**Por:**
- Juan Sebastián Ramírez 201923800
- Andrés Santiago Triana 201923265
- Gabriela García 201912531

## Instalación

Para realizar la instalación del API debe descargarlo y dirigirse a la carpeta en la que se encuentra ubicado.
En caso de no tener python3 y pip, debe instalarlo, pues es el lenguaje en el que se desarrolló el API.

Depues debe instalar las dependencias, para esto utilice el comando

    pip install -r requirements.txt

Ahora instale uvicorn con el siguiente comando

    pip install "uvicorn[standard]" 
   
   Para este punto el API debe estar instalada.

## Despliegue

Para desplegar el API dirijase a la carpeta en la que realizó las instalaciones y ejecute el comando 

    uvicorn main:app

Justo despues de esto debe poder ver el puerto en el que se está ejecutando el API. El puerto por defecto es el *8000*.

## Funcionamiento

Los dos URLs habilitadas:
1. */predict*
2. */evaluar*

Estas rutas deben ser corridas sobre la ruta en la que está corriendo el API (detallada en la consola al realizar el despliegue), lo común es entonces que las peticiones sean realizadas sobre las rutas *http://localhost:8000/predict* y *http://localhost:8000/evaluar*.

Las peticiones sobre estas rutas deben ser POST y el body debe contener; Para la primera ruta un JSON que contenga el escenario que se desea predecir, con los siguientes atributos y tipos de datos

    adult_mortality: float
    infant_deaths: float
    alcohol: float
    percentage_expenditure: float
    hepatitis_B: float
    measles: float
    bmi: float
    under_five_deaths: float
    polio: float
    total_expenditure: float
    diphtheria: float
    hiv_aids: float
    gdp: float
    population: float
    thinness_10_19_years: float
    thinness_5_9_years: float
    income_composition_of_resources : float
    schooling: float
Para la segunda ruta el body debe tener los mismos atributos pero tipo list y añadiendo el atributo `life_expectancy:list`.

En cuanto los resultados ambos constan de un JSON en el que para la ruta */predict* se llama "resultado" y para la ruta */evaluar* se llama "R^2".
