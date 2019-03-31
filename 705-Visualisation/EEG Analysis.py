
# coding: utf-8

# # CS705 Project Implementation: Data Visualisation
# <br>

# ### Module Imports
# Importing all required modules for data visualisation.

# In[1]:


import plotly as py
py.tools.set_credentials_file(username='ssin735',api_key='M2eZJJ4aN4Fz9W3XWo1w')

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


# <hr><br>
# ### Reading in original CSV data 
# - 5 minutes of data for each game: 512 Hz
# - Every second recorded is broken down into 512 further readings 
# - Overall approximately: 5 mins x 60 sec x 512 = 153600 rows of data

# #### Big Rigs: Over the Road Racing (Low Rated Game)

# In[2]:


origBR = pd.read_csv('C:/Users/Sabaoon Raza Khan/project-5-c/705-Visualisation/CSV-Data/BigRigs.csv', low_memory=False)


# #### Need for Speed: Hot Pursuit 2 (Average Rated Game)

# In[3]:


origHP = pd.read_csv('C:/Users/Sabaoon Raza Khan/project-5-c/705-Visualisation/CSV-Data/NFS-HP2.csv', low_memory=False)


# #### GTR 2: FIA GT Racing Game (High Rated Game)

# In[4]:


origGT = pd.read_csv('C:/Users/Sabaoon Raza Khan/project-5-c/705-Visualisation/CSV-Data/GTR2.csv', low_memory=False)


# <hr><br>
# ### Plotting original data:
# - Electrode: Raw signal data from Neurosky Mindwave device
# - Attention: Proprietary eSense signals built-in to the Mindwave device  
# - Meditation: Proprietary eSense signals built-in to the Mindwave device  

# #### Big Rigs: Over the Road Racing (Low Rated Game)

# In[5]:


br01 = go.Scatter(
                    y=origBR['Electrode'], x=origBR['Time:512Hz'], # Data
                    mode='lines', name='Electrode' # Additional options
                   )
br02 = go.Scatter(y=origBR['Attention'], x=origBR['Time:512Hz'], mode='lines', name='Attention' )
br03 = go.Scatter(y=origBR['Meditation'], x=origBR['Time:512Hz'], mode='lines', name='Meditation')

layout_br0 = go.Layout(title='Plot of Original Big Rigs CSV Data',
                   plot_bgcolor='rgb(230, 230, 230)')

fig_br0 = go.Figure(data=[br01, br02, br03], layout=layout_br0)

# Plot data in the notebook
py.iplot(fig_br0, filename='plot-from-orig-br0-csv')


# #### Need for Speed: Hot Pursuit 2 (Average Rated Game)

# In[6]:


hp01 = go.Scatter(
                    y=origHP['Electrode'], x=origHP['Time:512Hz'], # Data
                    mode='lines', name='Electrode' # Additional options
                   )
hp02 = go.Scatter(y=origHP['Attention'], x=origHP['Time:512Hz'], mode='lines', name='Attention' )
hp03 = go.Scatter(y=origHP['Meditation'], x=origHP['Time:512Hz'], mode='lines', name='Meditation')

layout_hp0 = go.Layout(title='Plot of Original Hot Pursuit CSV Data',
                   plot_bgcolor='rgb(230, 230, 230)')

fig_hp0 = go.Figure(data=[hp01, hp02, hp03], layout=layout_hp0)

# Plot data in the notebook
py.iplot(fig_hp0, filename='plot-from-orig-hp0-csv')


# #### GTR 2: FIA GT Racing Game (High Rated Game)

# In[7]:


gt01 = go.Scatter(
                    y=origGT['Electrode'], x=origGT['Time:512Hz'], # Data
                    mode='lines', name='Electrode' # Additional options
                   )
gt02 = go.Scatter(y=origGT['Attention'], x=origGT['Time:512Hz'], mode='lines', name='Attention' )
gt03 = go.Scatter(y=origGT['Meditation'], x=origGT['Time:512Hz'], mode='lines', name='Meditation')

layout_gt0 = go.Layout(title='Plot of Original GTR2 CSV Data',
                   plot_bgcolor='rgb(230, 230, 230)')

fig_gt0 = go.Figure(data=[gt01, gt02, gt03], layout=layout_gt0)

# Plot data in the notebook
py.iplot(fig_gt0, filename='plot-from-orig-gt0-csv')


# <hr><br>
# ### Averaging values for every second: 

# #### Big Rigs: Over the Road Racing (Low Rated Game)

# In[8]:


averagedBR = origBR.groupby(np.arange(len(origBR))//512).mean()

BR_table = FF.create_table(averagedBR.head())
py.iplot(BR_table, filename='BR-table')


# #### Need for Speed: Hot Pursuit 2 (Average Rated Game)

# In[9]:


averagedHP = origHP.groupby(np.arange(len(origHP))//512).mean()

HP_table = FF.create_table(averagedHP.head())
py.iplot(HP_table, filename='HP-table')


# #### GTR 2: FIA GT Racing Game (High Rated Game)

# In[10]:


averagedGT = origGT.groupby(np.arange(len(origGT))//512).mean()

GT_table = FF.create_table(averagedGT.head())
py.iplot(GT_table, filename='GT-table')


# <hr><br>
# ### Creating line data for each brainwave signal against time:

# #### Big Rigs: Over the Road Racing (Low Rated Game)

# In[11]:


brRaw = go.Scatter(
                    y=averagedBR['Electrode'], x=averagedBR['Time:512Hz'], # Data
                    mode='lines', name='Big Rigs Electrode' # Additional options
                   )
brAtt = go.Scatter(y=averagedBR['Attention'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs Attention' )
brMed = go.Scatter(y=averagedBR['Meditation'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs Meditation')
brDelta = go.Scatter(y=averagedBR['Delta'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs Delta')
brTheta = go.Scatter(y=averagedBR['Theta'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs Theta')
brLA = go.Scatter(y=averagedBR['Low Alpha'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs Low Alpha')
brHA = go.Scatter(y=averagedBR['High Alpha'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs High Alpha')
brLB = go.Scatter(y=averagedBR['Low Beta'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs Low Beta')
brHB = go.Scatter(y=averagedBR['High Beta'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs High Beta')
brLG = go.Scatter(y=averagedBR['Low Gamma'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs Low Gamma')
brMG = go.Scatter(y=averagedBR['Mid Gamma'], x=averagedBR['Time:512Hz'], mode='lines', name='Big Rigs Mid Gamma')


# #### Need for Speed: Hot Pursuit 2 (Average Rated Game)

# In[12]:


hpRaw = go.Scatter(
                    y=averagedHP['Electrode'], x=averagedHP['Time:512Hz'], # Data
                    mode='lines', name='Hot Pursuit Electrode' # Additional options
                   )
hpAtt = go.Scatter(y=averagedHP['Attention'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit Attention' )
hpMed = go.Scatter(y=averagedHP['Meditation'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit Meditation')
hpDelta = go.Scatter(y=averagedHP['Delta'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit Delta')
hpTheta = go.Scatter(y=averagedHP['Theta'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit Theta')
hpLA = go.Scatter(y=averagedHP['Low Alpha'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit Low Alpha')
hpHA = go.Scatter(y=averagedHP['High Alpha'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit High Alpha')
hpLB = go.Scatter(y=averagedHP['Low Beta'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit Low Beta')
hpHB = go.Scatter(y=averagedHP['High Beta'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit High Beta')
hpLG = go.Scatter(y=averagedHP['Low Gamma'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit Low Gamma')
hpMG = go.Scatter(y=averagedHP['Mid Gamma'], x=averagedHP['Time:512Hz'], mode='lines', name='Hot Pursuit Mid Gamma')


# #### GTR 2: FIA GT Racing Game (High Rated Game)

# In[13]:


gtRaw = go.Scatter(
                    y=averagedGT['Electrode'], x=averagedGT['Time:512Hz'], # Data
                    mode='lines', name='GTR2 Electrode' # Additional options
                   )
gtAtt = go.Scatter(y=averagedGT['Attention'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 Attention' )
gtMed = go.Scatter(y=averagedGT['Meditation'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 Meditation')
gtDelta = go.Scatter(y=averagedGT['Delta'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 Delta')
gtTheta = go.Scatter(y=averagedGT['Theta'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 Theta')
gtLA = go.Scatter(y=averagedGT['Low Alpha'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 Low Alpha')
gtHA = go.Scatter(y=averagedGT['High Alpha'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 High Alpha')
gtLB = go.Scatter(y=averagedGT['Low Beta'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 Low Beta')
gtHB = go.Scatter(y=averagedGT['High Beta'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 High Beta')
gtLG = go.Scatter(y=averagedGT['Low Gamma'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 Low Gamma')
gtMG = go.Scatter(y=averagedGT['Mid Gamma'], x=averagedGT['Time:512Hz'], mode='lines', name='GTR2 Mid Gamma')


# <hr><br>
# ### Plotting data averaged for every second:

# #### Big Rigs: Over the Road Racing (Low Rated Game)

# In[14]:


layout_brAvg = go.Layout(title='Plot of Averaged Big Rigs Data',
                   plot_bgcolor='rgb(230, 230, 230)')

fig_brAvg = go.Figure(data=[brRaw, brAtt, brMed], layout=layout_brAvg)

# Plot data in the notebook
py.iplot(fig_brAvg, filename='plot-from-brAvg-csv')


# #### Need for Speed: Hot Pursuit 2 (Average Rated Game)

# In[15]:


layout_hpAvg = go.Layout(title='Plot of Averaged Hot Pursuit Data',
                   plot_bgcolor='rgb(230, 230, 230)')

fig_hpAvg = go.Figure(data=[hpRaw, hpAtt, hpMed], layout=layout_hpAvg)

# Plot data in the notebook
py.iplot(fig_hpAvg, filename='plot-from-hpAvg-csv')


# #### GTR 2: FIA GT Racing Game (High Rated Game)

# In[16]:


layout_gtAvg = go.Layout(title='Plot of Averaged GTR2 Data',
                   plot_bgcolor='rgb(230, 230, 230)')

fig_gtAvg = go.Figure(data=[gtRaw, gtAtt, gtMed], layout=layout_gtAvg)

# Plot data in the notebook
py.iplot(fig_gtAvg, filename='plot-from-gtAvg-csv')


# <hr><br>
# ### Engagement Calculation:
# - Findings by [1] suggest Index 1 [(Global Beta / (Global Alpha + Global Theta)] is the preferred algorithm for calculating the engagement levels of players playing video games.
# - So, this is the formula we'll be using to calculate player engagement levels amongst different rated games.
# 
# Reference: 
# - [1] McMahan, T., Parberry, I., & Parsons, T. D. (2015, June). Evaluating Electroencephalography Engagement Indices During Video Game Play. In FDG.

# In[17]:


brEng = go.Scatter(
                    y=(averagedBR['Low Beta'] + averagedBR['High Beta'])/
                      (averagedBR['Theta'] + 
                       (averagedBR['Low Alpha'] + averagedBR['High Alpha'])), 
                    x=averagedBR['Time:512Hz'], # Data
                    mode='lines', name='Big Rigs Engagement' # Additional options
                   )

hpEng = go.Scatter(
                    y=(averagedHP['Low Beta'] + averagedHP['High Beta'])/
                      (averagedHP['Theta'] + 
                       (averagedHP['Low Alpha'] + averagedHP['High Alpha'])), 
                    x=averagedHP['Time:512Hz'], # Data
                    mode='lines', name='Hot Pursuit Engagement' # Additional options
                   )


gtEng = go.Scatter(
                    y=(averagedGT['Low Beta'] + averagedGT['High Beta'])/
                      (averagedGT['Theta'] + 
                       (averagedGT['Low Alpha'] + averagedGT['High Alpha'])), 
                    x=averagedGT['Time:512Hz'], # Data
                    mode='lines', name='GTR2 Engagement' # Additional options
                   )

gameEng = go.Layout(title='Engagement Data',
                   plot_bgcolor='rgb(230, 230, 230)')

fig_Eng = go.Figure(data=[hpEng, brEng, gtEng], layout=gameEng)

# Plot data in the notebook
py.iplot(fig_Eng, filename='plot-from-eng-csv')

