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

#%% test

def greet():
    return "Hello from Mackenley!"

#%%

