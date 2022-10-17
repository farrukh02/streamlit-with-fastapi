import json
import pickle
import pyreadstat
import httpx
from fastapi import FastAPI
from fastapi.logger import logger
from pydantic import BaseModel
import pandas as pd
import uvicorn


# Creating a class for the attributes input to the ML model.
app = FastAPI()
class dic(BaseModel):
    dic = {}
    dic["ord_T_q_9101a_3"]: int
    dic["ord_T_q_9101a_4"]: int
    dic["ord_T_q_9101a_5"]: int
    dic["ord_T_q_9101a_7"]: int
    dic["ord_T_q_9101a_8"]: int
    dic["ord_T_q_9101b_1"]: int
    dic["ord_T_q_9101b_2"]: int
    dic["ord_T_q_9101b_3"]: int
    dic["ord_T_q_9101b_4"]: int
    dic["ord_T_q_9101b_6"]: int
    dic["ord_T_q_9101b_7"]: int
    dic["ord_T_q_9101c_1"]: int
    dic["ord_T_q_9101c_2"]: int
    dic["ord_T_q_9101c_4"]: int
    dic["ord_T_q_9101c_6"]: int
    dic["ord_T_q_9101c_7"]: int
    dic["ord_T_q_9101c_8"]: int
    dic["ord_T_q_9101c_9"]: int
    dic["ord_T_q_9101d_2"]: int
    dic["ord_T_q_9101d_3"]: int
    dic["ord_T_q_9101d_4"]: int
    dic["ord_T_q_9101d_6"]: int
    dic["ord_T_q_9101d_7"]: int
    dic["ord_T_q_9101d_8"]: int
    dic["ord_T_q_9101d_9"]: int
    dic["ord_T_q_9101e_1"]: int
    dic["ord_T_q_9101e_2"]: int
    dic["ord_T_q_9101e_4"]: int
    dic["ord_T_q_9101e_7"]: int
    dic["ord_T_q_9101e_8"]: int
    dic["ord_T_q_9101f_2"]: int
    dic["ord_q_9301"]: int
    dic["nom_q_1102_Man"]: int
    dic["nom_q_1102_Women"]: int
    dic["nom_q_1111_Dushanbe"]: int
    dic["nom_q_1111_GBAO"]: int
    dic["nom_q_1111_Khatlon"]: int
    dic["nom_q_1111_Sogd"]: int
    dic["nom_q_1111_Subordination of the center"]: int
    dic["nom_q_1110_City"]: int
    dic["nom_q_1110_Village"]: int
    dic["nom_q_9103b_Chemistry"]: int
    dic["nom_q_9103b_Electronics"]: int
    dic["nom_q_9103c_Botany"]: int
    dic["nom_q_9103c_Photography"]: int
    dic["nom_q_9103d_Advice on work"]: int
    dic["nom_q_9103d_Owning a store"]: int
    dic["nom_q_9103e_Company management"]: int
    dic["nom_q_9103e_Helping families in need"]: int
    dic["nom_q_9103f_Doktor"]: int
    dic["nom_q_9103f_Physical training"]: int
    dic["nom_q_9103g_Music"]: int
    dic["nom_q_9103g_Working with wood"]: int
    dic["nom_q_9103h_Economic sciences"]: int
    dic["nom_q_9103h_Physics"]: int
    dic["nom_q_9103i_Art"]: int
    dic["nom_q_9103i_Education"]: int
    dic["nom_q_9103j_Artist / Folk Crafts"]: int
    dic["nom_q_9103j_Law"]: int
    dic["nom_q_9103k_Child care"]: int
    dic["nom_q_9103k_Stand electronics"]: int
    dic["nom_q_9103l_Landscaping"]: int
    dic["nom_q_9103l_Playing in a group, being a member of a music team"]: int
    dic["nom_q_9103m_Mechanic"]: int
    dic["nom_q_9103m_Travel agent"]: int
    dic["nom_q_9103n_Picture description"]: int
    dic["nom_q_9103n_Work in the office"]: int
    dic["nom_q_9103o_Forest"]: int
    dic["nom_q_9103o_The nurse of mercy"]: int
    dic["nom_q_9103p_Economist"]: int
    dic["nom_q_9103p_Electric"]: int
    dic["nom_q_9103q_Accounting"]: int
    dic["nom_q_9103q_Geology"]: int
    dic["nom_q_9103r_Builder"]: int
    dic["nom_q_9103r_Economist"]: int
    dic["nom_q_9103s_Confirmation of a home loan (mortgage)"]: int
    dic["nom_q_9103s_Helping patients in the hospital"]: int
    dic["nom_q_9303_Dead"]: int
    dic["nom_q_9303_Does not work due to limited physical ability or illness"]: int
    dic["nom_q_9303_Doing housework (including caring for children)"]: int
    dic["nom_q_9303_Entrepreneur / employee with self-account / private entrepreneur / employer (yes)"]: int
    dic["nom_q_9303_I don't know / Rejection"]: int
    dic["nom_q_9303_Official / Registered Employee (NOT YOUR FAMILY BUSINESS)"]: int
    dic["nom_q_9303_Retired"]: int
    dic["nom_q_9303_Unemployed (ready to work and looking for work)"]: int
    dic["nom_q_9303_Unofficial / unregistered employee (NOT YOUR FAMILY BUSINESS)"]: int
    dic["nom_q_9303_Work as an employee or assistant on a farm (farm, h"]: int
    dic["nom_q_9303_Working as an employee or assistant in a NON-agricultural business / m"]: int
    dic["nom_q_9305_Complete general secondary education (Grades 10-11)"]: int
    dic["nom_q_9305_General Primary Education (Grades 1-4)"]: int
    dic["nom_q_9305_Higher Education (University, Conservatory, Academy) or Postgraduate, d"]: int
    dic["nom_q_9305_I don't know / Rejection"]: int
    dic["nom_q_9305_Incomplete general secondary education (Grades 5-9)"]: int
    dic["nom_q_9305_Primary vocational education (VET) or secondary vocational education (technical school)"]: int
    dic["nom_q_9305_Without formal education"]: int
    dic["nom_q_9306_Dead"]: int
    dic["nom_q_9306_Does not work due to limited physical ability or illness"]: int
    dic["nom_q_9306_Doing housework (including caring for children)"]: int
    dic["nom_q_9306_Entrepreneur / employee with self-account / private entrepreneur / employer (yes)"]: int
    dic["nom_q_9306_I don't know / Rejection"]: int
    dic["nom_q_9306_Retired"]: int
    dic["nom_q_9306_Unemployed (ready to work and looking for work)"]: int
    dic["nom_q_9306_Unofficial / unregistered employee (NOT YOUR FAMILY BUSINESS)"]: int
    dic["nom_q_9306_Work as an employee or assistant on a farm (farm, h"]: int
    dic["nom_q_9306_Working as an employee or assistant in a NON-agricultural business / m"]: int
    dic["nom_q_9306_Yes, more than 10 years"]: int
    dic["nom_q_9308_Full secondary education (grades 10-11)"]: int
    dic["nom_q_9308_General primary education (grades 1-4)"]: int
    dic["nom_q_9308_Higher education (University, Conservatory, Academy) or Postgraduate studies, etc"]: int
    dic["nom_q_9308_Incomplete general secondary education (grades 5-9)"]: int
    dic["nom_q_9308_Primary vocational education (vocational school) or secondary vocational (Technical school)"]: int
    dic["nom_q_9308_Without formal education"]: int
    dic["nom_q_9308_don't know / Denial"]: int


with open("last_model.pickle", "rb") as f:
    loaded_model = pickle.load(f)


@app.get('/')
def get_potability(data: dic):
    received = data.dict()
    mp = []
    for i in received.columns:
        mp[i] = received["i"]
    output = loaded_model.predict_proba(mp[0:1]).tolist()[0]
    return  output


