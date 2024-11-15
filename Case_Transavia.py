#%% Importeer de benodigde bibliotheken
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import os
import requests
import folium
from PIL import Image
from streamlit_folium import st_folium 
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap
from sklearn.ensemble import RandomForestRegressor

import ARGENIS.ARGN as ar
import MACKENLEY.MACK as ma
import JADEN.JAD as jd
import CHRISTIAN.CHRIS as ch

#%% test

print(ar.greet())
print(ma.greet())
print(jd.greet())
print(ch.greet())
print(ma.say_hello())



#%% Dashboard layout
#cde

