from fastapi import FastAPI
from fastapi.responses import FileResponse,JSONResponse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import Statistical_Summary
import visualization
import Correlation_Analysis
import line

df = pd.read_csv('energy_dataset_.csv')

app = FastAPI()


@app.get("/api/summary/{function_name}")
async def summary(function_name:str):
        if function_name == 'details':
           return Statistical_Summary.summary
        elif function_name == 'mean':
           return Statistical_Summary.mean
        elif function_name == 'median':
           return Statistical_Summary.median
        elif function_name == 'mode':
           return Statistical_Summary.mode
        elif function_name == 'range':
           return Statistical_Summary.range
        elif function_name == 'variance':
           return Statistical_Summary.variance
        else:
           return 'Wrong Entry!!! Please check details/mean/median/mode/range or variance'
        
        
@app.get("/api/visualization",response_class=JSONResponse)
async def visual(type:str,variable:str):
   com = visualization.ash(type,variable)
   return JSONResponse(content=com)

@app.get('/api/line_graphs',response_class=JSONResponse)
async def line():
   return JSONResponse(content=line.lines())

@app.get('/api/correlations/{plot_type}',response_class=JSONResponse)
async def corr(plot_type):
   if plot_type == 'heat_map':
     return JSONResponse(Correlation_Analysis.heat_map())
   elif plot_type == 'scatter_plot_matrix':
      return JSONResponse(Correlation_Analysis.corr_scatter())
   else:
      return 'check neither heat_map or scatter_plot_matrix'



