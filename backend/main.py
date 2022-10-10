import json
import pickle

import httpx
from fastapi import Body, FastAPI
from fastapi.logger import logger
from pydantic import BaseModel

app = FastAPI()

# Creating a class for the attributes input to the ML model.
class WaterMetrics(BaseModel):
    nom_q_9103f : int
    nom_q_9103o : int
    nom_q_9103b : int
    nom_q_9103k : int
    nom_q_9103s : int
    nom_q_9103h : int
    nom_q_9103c : int
    nom_q_9103l : int
    nom_q_9103j : int
    nom_q_9103q : int
    nom_q_9103m : int
    nom_q_9103p : int
    nom_q_9103g : int
    nom_q_9103e : int
    nom_q_9103r : int
    nom_q_9103n : int
    nom_q_9103d : int
    nom_q_9103i : int
    ord_T_q_9101c_1 : int
    ord_T_q_9101e_7 : int
    ord_T_q_9101a_7 : int
    ord_T_q_9101d_9 : int
    ord_T_q_9101a_8 : int
    ord_T_q_9101f_2 : int
    ord_T_q_9101d_2 : int
    ord_T_q_9101c_4 : int
    ord_T_q_9101d_3 : int
    ord_T_q_9101c_9 : int
    ord_T_q_9101d_4 : int
    ord_T_q_9101c_7 : int
    ord_T_q_9101b_3 : int
    ord_T_q_9101b_2 : int
    ord_T_q_9101e_8 : int
    ord_T_q_9101a_5 : int
    ord_T_q_9101a_3 : int
    ord_T_q_9101b_6 : int
    ord_T_q_9101e_4 : int
    ord_T_q_9101b_7 : int
    ord_T_q_9101a_4 : int
    ord_T_q_9101c_8 : int
    ord_T_q_9101c_2 : int
    ord_T_q_9101c_6 : int
    ord_T_q_9101d_7 : int
    ord_T_q_9101e_2 : int
    ord_T_q_9101e_1 : int
    ord_T_q_9101d_6 : int
    ord_T_q_9101d_8 : int
    ord_T_q_9101b_1 : int
    ord_T_q_9101b_4 : int


# Loading the trained model
with open("final_cluster.pickle", "rb") as f:
    loaded_model = pickle.load(f)

# Sending a post request to the “/prediction” route with a request body. 
# The request body contains the key-value pairs of the water metrics parameters

@app.post('/prediction' )
def get_potability(data: WaterMetrics):
    received = data.dict()
    nom_q_9103f = received['nom_q_9103f']
    nom_q_9103o = received['nom_q_9103o']
    nom_q_9103b = received['nom_q_9103b']
    nom_q_9103k = received['nom_q_9103k']
    nom_q_9103s = received['nom_q_9103s']
    nom_q_9103h = received['nom_q_9103h']
    nom_q_9103c = received['nom_q_9103c']
    nom_q_9103l = received['nom_q_9103l']
    nom_q_9103j = received['nom_q_9103j']
    nom_q_9103q = received['nom_q_9103q']
    nom_q_9103m = received['nom_q_9103m']
    nom_q_9103p = received['nom_q_9103p']
    nom_q_9103g = received['nom_q_9103g']
    nom_q_9103e = received['nom_q_9103e']
    nom_q_9103r = received['nom_q_9103r']
    nom_q_9103n = received['nom_q_9103n']
    nom_q_9103d = received['nom_q_9103d']
    nom_q_9103i = received['nom_q_9103i']
    ord_T_q_9101c_1 = received['ord_T_q_9101c_1']
    ord_T_q_9101e_7 = received['ord_T_q_9101e_7']
    ord_T_q_9101a_7 = received['ord_T_q_9101a_7']
    ord_T_q_9101d_9 = received['ord_T_q_9101d_9']
    ord_T_q_9101a_8 = received['ord_T_q_9101a_8']
    ord_T_q_9101f_2 = received['ord_T_q_9101f_2']
    ord_T_q_9101d_2 = received['ord_T_q_9101d_2']
    ord_T_q_9101c_4 = received['ord_T_q_9101c_4']
    ord_T_q_9101d_3 = received['ord_T_q_9101d_3']
    ord_T_q_9101c_9 = received['ord_T_q_9101c_9']
    ord_T_q_9101d_4 = received['ord_T_q_9101d_4']
    ord_T_q_9101c_7 = received['ord_T_q_9101c_7']
    ord_T_q_9101b_3 = received['ord_T_q_9101b_3']
    ord_T_q_9101b_2 = received['ord_T_q_9101b_2']
    ord_T_q_9101e_8 = received['ord_T_q_9101e_8']
    ord_T_q_9101a_5 = received['ord_T_q_9101a_5']
    ord_T_q_9101a_3 = received['ord_T_q_9101a_3']
    ord_T_q_9101b_6 = received['ord_T_q_9101b_6']
    ord_T_q_9101e_4 = received['ord_T_q_9101e_4']
    ord_T_q_9101b_7 = received['ord_T_q_9101b_7']
    ord_T_q_9101a_4 = received['ord_T_q_9101a_4']
    ord_T_q_9101c_8 = received['ord_T_q_9101c_8']
    ord_T_q_9101c_2 = received['ord_T_q_9101c_2']
    ord_T_q_9101c_6 = received['ord_T_q_9101c_6']
    ord_T_q_9101d_7 = received['ord_T_q_9101d_7']
    ord_T_q_9101e_2 = received['ord_T_q_9101e_2']
    ord_T_q_9101e_1 = received['ord_T_q_9101e_1']
    ord_T_q_9101d_6 = received['ord_T_q_9101d_6']
    ord_T_q_9101d_8 = received['ord_T_q_9101d_8']
    ord_T_q_9101b_1 = received['ord_T_q_9101b_1']
    ord_T_q_9101b_4 = received['ord_T_q_9101b_4']
    Turbidity = received['Turbidity']
    pred_name = loaded_model.predict_proba([[nom_q_9103f,nom_q_9103o,nom_q_9103b,nom_q_9103k,
                                 nom_q_9103s,nom_q_9103h,nom_q_9103c,nom_q_9103l,nom_q_9103j,
                                 nom_q_9103q,nom_q_9103m,nom_q_9103p,nom_q_9103g,nom_q_9103e,nom_q_9103r,nom_q_9103n,nom_q_9103d,nom_q_9103i,
                                 ord_T_q_9101c_1,ord_T_q_9101e_7,ord_T_q_9101a_7,ord_T_q_9101d_9,ord_T_q_9101a_8,ord_T_q_9101f_2,ord_T_q_9101d_2,
                                 ord_T_q_9101c_4,ord_T_q_9101d_3,ord_T_q_9101c_9,ord_T_q_9101d_4,ord_T_q_9101c_7,ord_T_q_9101b_3,ord_T_q_9101b_2,
                                 ord_T_q_9101e_8,ord_T_q_9101a_5,ord_T_q_9101a_3,ord_T_q_9101b_6,ord_T_q_9101e_4,ord_T_q_9101b_7,ord_T_q_9101a_4,
                                 ord_T_q_9101c_8,ord_T_q_9101c_2,ord_T_q_9101c_6,ord_T_q_9101d_7,ord_T_q_9101e_2,ord_T_q_9101e_1,ord_T_q_9101d_6,
                                 ord_T_q_9101d_8,ord_T_q_9101b_1,ord_T_q_9101b_4]]).tolist()[0]
    return pred_name
    



@app.get("/get_entities/{id}")
async def get_entities(id:str ):
    
    url="http://orion.docker:1026/ngsi-ld/v1/entities/" +  id + "?options=keyValues"

    client = httpx.Client()
    response = client.get(url)
    
    logger.info(response.json())
    return response.json()

@app.patch("/prediction/{id}/{potability}")
def notify_prediction(id:str,potability:str):
    url = "http://orion.docker:1026/ngsi-ld/v1/entities/" + id + "/attrs/Potability"

    payload = json.dumps({
	"value": potability,
	"type": "Property"
	})
    headers = {
	'Content-Type': 'application/json',
	'Link': '<http://context/ngsi-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"'
	}
    client = httpx.Client()
    response = client.patch(url, headers=headers, data=payload)

    return response.json()


# homepage route
@app.get("/")
def read_root():
	return {'message': 'This is the homepage of the API '}



