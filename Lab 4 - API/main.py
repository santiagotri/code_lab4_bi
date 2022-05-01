from typing import Optional
from fastapi import FastAPI
import h11
from joblib import load
import pandas as pd
from DataModel import DataModel
from DataModel_mejorado import DataModelMejorado

app = FastAPI()


@app.get("/test")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
   print( "\nDatamodel:"+str(dataModel) + "\n\n")
   print("dict():" +str(dataModel.dict())+"\n\n")
   print("dict().keys():" +str(dataModel.dict().keys())+"\n\n")
   
   print(str(dataModel.dict().keys()))
   df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
   df.columns = dataModel.columns()
   model = load("assets/model.joblib")
   result = model.predict(df)
   return {"resultado":str(result[0])}

@app.post("/evaluar")
def evaluar(dataModel: DataModelMejorado):

   #print( "\nDatamodel:"+str(dataModel) + "\n\n")
   #print("dict():" +str(dataModel.dict())+"\n\n")
   #print("dict().keys():" +str(dataModel.dict().keys())+"\n\n")
   columna_predict = "Life expectancy"
   df1 = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys())
   df1.columns = dataModel.columns()
   x = df1.drop(columna_predict, axis=1)
   y = df1[columna_predict]
   
   #print( "\n x:" + str(x) + "\n")
   #print( "\n y:" + str(y) + "\n")
   
   model = load("assets/model.joblib")
   model.fit(x,y)
   rta = model.score(x,y)
   #print(str(rta))
   return({"R^2":rta})
