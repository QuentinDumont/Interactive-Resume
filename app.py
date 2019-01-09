# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from components import Header, make_dash_table, print_button

import pandas as pd

app = dash.Dash(__name__)
server = app.server

# read data for tables (one df per table)
df_fund_facts = pd.read_csv('data/df_contact_details.csv', encoding= 'latin1')
df_price_perf = pd.read_csv('data/df_price_perf.csv')
df_resume = pd.read_csv('data/df_resume.csv', encoding= 'latin1', sep = ';', header = None)
df_current_prices = pd.read_csv('data/df_current_prices.csv')
df_hist_prices = pd.read_csv('data/df_hist_prices.csv')
df_avg_returns = pd.read_csv('data/df_avg_returns.csv')
df_after_tax = pd.read_csv('data/df_after_tax.csv')
df_recent_returns = pd.read_csv('data/df_recent_returns.csv')
df_equity_char = pd.read_csv('data/df_equity_char.csv')
df_equity_diver = pd.read_csv('data/df_equity_diver.csv')
df_expenses = pd.read_csv('data/df_expenses.csv')
df_minimums = pd.read_csv('data/df_minimums.csv')
df_dividend = pd.read_csv('data/df_dividend.csv')
df_realized = pd.read_csv('data/df_realized.csv')
df_unrealized = pd.read_csv('data/df_unrealized.csv')
df_graph = pd.read_csv("data/df_graph.csv")
df_loc_resume = pd.read_csv('data/df_loc_resume.csv')
df_loc_resume_stu = df_loc_resume[df_loc_resume['Type'] == 'Studies']
df_loc_resume_pro = df_loc_resume[df_loc_resume['Type'] == 'Work']
stock_exc_goog = pd.read_csv('data/stock_google.csv', index_col = 0)
stock_exc_apple = pd.read_csv('data/stock_apple.csv', index_col = 0)
stock_exc_micro = pd.read_csv('data/stock_micro.csv', index_col = 0)
stock_exc_amzn = pd.read_csv('data/stock_amzn.csv', index_col = 0)
resume_hover = pd.read_csv('data/df_resume_hover.csv')
resume_hover_s = resume_hover[resume_hover['TYPE'] == 's']
resume_hover_w = resume_hover[resume_hover['TYPE'] == 'w']

#Data Page 1 - Map Prof & Educational
data_geo_stu = go.Scattermapbox(
    lat = df_loc_resume_stu['Lat'],
    lon = df_loc_resume_stu['Lon'],
    name = 'Education',
    text = [str(df_loc_resume_stu['PLACE'].iloc[n]) + '<br>' +
                '<br>' +
                str(df_loc_resume_stu['Position'].iloc[n]) + '<br>' 
            + str(df_loc_resume_stu['Duration'].iloc[n])
                
                for n in range(0,len(df_loc_resume_stu['Position']))],
    
    hoverinfo = 'text',
    marker=dict(
            size=11,
            color='blue',
    opacity = 0.8))

data_geo_pro = go.Scattermapbox(
    lat = df_loc_resume_pro['Lat'],
    lon = df_loc_resume_pro['Lon'],
    name = 'Pro. Exp.',
    text = [str(df_loc_resume_pro['PLACE'].iloc[n]) + '<br>' +
            str(df_loc_resume_pro['Position'].iloc[n]) + '<br>' +
            '<br>' +
            str(df_loc_resume_pro['Project / Department'].iloc[n]) + '<br>' +
            str(df_loc_resume_pro['Duration'].iloc[n])
                
                for n in range(0,len(df_loc_resume_pro['Position']))],
    
    hoverinfo = 'text',
    marker=dict(
            size=11,
            color='red',
    opacity = 0.8))

layout_geo = go.Layout(
    autosize=True,
    hovermode='closest',
    width =  340,
    height =  200,
    mapbox=dict(
        accesstoken='pk.eyJ1IjoicWR1bW9udCIsImEiOiJjam9yOTRldWswYzV2M2tsaHY5YXZzNG0zIn0.0umivpB2Czf02s2kurbyRg',
        style='light',
        center=dict(
            lat=10,
            lon=75
        ),
        zoom=-1
    ),
    margin=go.layout.Margin(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=4)
)


#Data Page 1  - Bar Chart Skills

skill_1 = go.Bar(
    x=['Excel', 'Python', 'SQL'],
    y=[90, 80, 60],
    text = ['Excel', 'Python', 'SQL'],
    name='Technical',
    textposition = 'auto',
    marker=dict(
        color='#43AA8B',
        opacity = 0.7,
        line=dict(
        color='#43AA8B',
        width=2)
        )
    )
skill_2 = go.Bar(
    x=[ 'Team-Player', 'Analyst', 'Problem-Solver'],
    y=[100, 95, 66],
    text = [ 'Team-Player', 'Analyst', 'Problem-Solver'],
    textposition = 'auto',
    name='Personal',
    marker=dict(
        color='#B2B09B',
                opacity = 0.7,
        line=dict(
        color='#B2B09B',
            width=2)
        )
    )
skill_3 = go.Bar(
    x=['French', 'English', 'German'],
    y=[100, 95, 33],
    text = ['French', 'English', 'German'],
    textposition = 'auto',
    name='Language',
    marker=dict(
        color="#EF3054",
        opacity = 0.7,
        line=dict(
        color="#EF3054",
        width=2)
        )
    )

#Chartfor Skill Page


stock_graph_google = go.Scatter(
x = stock_exc_goog.index,
y = stock_exc_goog['4. close'],
name = 'Google')

stock_graph_apple = go.Scatter(
x = stock_exc_apple.index,
y = stock_exc_apple['4. close'],
name = 'Apple')

stock_graph_micro = go.Scatter(
x = stock_exc_micro.index,
y = stock_exc_micro['4. close'],
name = 'Microsoft')

stock_graph_amzn = go.Scatter(
x = stock_exc_amzn.index,
y = stock_exc_amzn['4. close'],
name = 'Amazon')

data_stock = [stock_graph_google, stock_graph_apple, stock_graph_micro, stock_graph_amzn]

layout_stock = dict(
    height = 350,
    title='Stock Options',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count = 1,
                    label = '1y',
                    step = 'year',
                    stepmode = 'backward'),
                dict(count = 5,
                    label = '5y',
                    step = 'year',
                    stepmode = 'backward'),
                dict(count = 10,
                    label = '10y',
                    step = 'year',
                    stepmode = 'backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible = False
        ),
        type='date'
    ),
    yaxis = dict(title = 'Closing Value'),
)

#Figure
data_hover_w = go.Scatter(
x = resume_hover_w.x,
y = resume_hover_w.y,
name = 'Jobs',
mode = 'markers',
text = [resume_hover_w['Position'].iloc[i] for i in range(0, len(resume_hover_w['Position']))],
hoverinfo ='text+name',
marker = dict(size = [35,32,26,23,20,18,16],
             color = '#43AA8B'))

data_hover_s = go.Scatter(
x = resume_hover_s.x,
y = resume_hover_s.y,
name = 'Studies',
mode = 'markers',
text = [resume_hover_s['Position'].iloc[i] for i in range(0, len(resume_hover_s['Position']))],
hoverinfo ='text+name',
marker = dict(size = 30,
             color='#EF3054'))

layout_hover = {
    'hovermode': 'closest',
    'margin' : go.layout.Margin(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    )}

figure_hover = {'data' : [data_hover_w], 'layout' : layout_hover}


#Chart Page Profesional Skills / Bar Chart
chart_soft_skills_0 = go.Bar(
  x = ['Project Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem Solving Skills', 'Python', 'SQL'],
  y = [1.1,0.1,0.4,0.5,0.6,0.5,0.1,0.1],
  name = 'Soft Skills',
  text = ['Project <br> Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem <br> Solving <br> Skills', 'Python', 'SQL'],
  textposition = 'auto',
  marker=dict(
    color="#43AA8B",
    opacity = 0.7,
    line=dict(
      color='red',
      width=5)
    ))

chart_soft_skills_1 = go.Bar(
  x = ['Project Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem Solving Skills', 'Python', 'SQL', 'Python', 'SQL'],
  y = [2.5,0.5,0.7,0.6,0.9,0.7,0.1,0.1],
  name = 'Soft Skills',
  text = ['Project <br> Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem <br> Solving <br> Skills', 'Python', 'SQL'],
  textposition = 'auto',
  marker=dict(
    color="#43AA8B",
    opacity = 0.7,
    line=dict(
      color='red',
      width=5)
    ))

chart_soft_skills_2 = go.Bar(
  x = ['Project Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem Solving Skills', 'Python', 'SQL', 'Python', 'SQL'],
  y = [3.6,1.4,1.1,0.9,1.2,1,0.1,0.1],
  name = 'Soft Skills',
  text = ['Project <br> Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem <br> Solving <br> Skills', 'Python', 'SQL'],
  textposition = 'auto',
  marker=dict(
    color="#43AA8B",
    opacity = 0.7,
    line=dict(
      color='red',
      width=5)
    ))

chart_soft_skills_3 = go.Bar(
  x = ['Project Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem Solving Skills', 'Python', 'SQL', 'Python', 'SQL'],
  y = [5.5,4.2,3,4.0,5,3.5,0.1,0.1],
  name = 'Soft Skills',
  text = ['Project <br> Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem <br> Solving <br> Skills', 'Python', 'SQL'],
  textposition = 'auto',
  marker=dict(
    color="#43AA8B",
    opacity = 0.7,
    line=dict(
      color='red',
      width=5)
    ))

chart_soft_skills_4 = go.Bar(
  x = ['Project Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem Solving Skills', 'Python', 'SQL', 'Python', 'SQL'],
  y = [8.7,7,4.9,6,4.7,6.3,0.1,0.1],
  name = 'Soft Skills',
  text = ['Project <br> Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem <br> Solving <br> Skills', 'Python', 'SQL'],
  textposition = 'auto',
  marker=dict(
    color="#43AA8B",
    opacity = 0.7,
    line=dict(
      color='red',
      width=5)
    ))

chart_soft_skills_5 = go.Bar(
  x = ['Project Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem Solving Skills', 'Python', 'SQL', 'Python', 'SQL'],
  y = [9.3,9.1,6.3,5.4,6.9,7.5,7,3.2],
  name = 'Soft Skills',
  text = ['Project <br> Management', 'Excel', 'Management', 'Communication', 'Analysis', 'Problem <br> Solving <br> Skills', 'Python', 'SQL'],
  textposition = 'auto',
  marker=dict(
    color="#43AA8B",
    opacity = 0.7,
    line=dict(
      color='red',
      width=5)
    ))

layout_soft_skills = go.Layout(
    barmode = 'stack',
    bargap=0.1,
    bargroupgap=0.1,
    xaxis=dict(
        autorange=True,
        showgrid=False,
        zeroline=True,
        showline=True,
        showticklabels=False),
    yaxis =
    dict(
        autorange=True,
        zeroline=True,
        showline=True,
        tickmode = 'array',
        tickvals = [1, 4, 9],
        ticktext = ['BEGINNER', 'GOOD', 'PRO'],
        showticklabels = True,
        tickfont = {'size' : 10},
        
    ),
        margin=go.layout.Margin(
        r=0,
        b=0,
        t=0,
        pad=0),
    legend=dict(
        x= -0.1,
        y =0.002,
        traceorder='normal',
        font=dict(
            family='sans-serif',
            size=8,
            color='#000'
        ),
        bgcolor='#E2E2E2',
        bordercolor='#FFFFFF',
        borderwidth=2,
        orientation="h"
    )
)

figure_soft_skill = {'data' : [chart_soft_skills_0], 'layout' : layout_soft_skills}

## Page layouts
overview = html.Div([  # page 1

        print_button(),

        html.Div([
            Header(),

            # Row 3
            html.Div([

                html.Div([
                    html.H6('Candidate Summary',
                            className="gs-header gs-text-header padded"),

                    html.Br([]),

                    html.P(style = {'text-align' : 'justify'},
                      children = ["\
                            With four years of experience in coordinating international projects, \
                            from conception to completion. I own a Master’s degree in International Management. \
                            Considered as  a self-initiated, goal-oriented and organized personality, \
                            I wish to deepen my expertise within the Data field (BI tools, Viz, Stock, etc).  \
                            "]),

                ], className="six columns"),

                html.Div([
                    html.H6(["Contact Details"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_fund_facts))
                ], className="six columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6('Professional Experiences & Education',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(
                        id = "graph-1",
                        figure = dict(data=[data_geo_stu, data_geo_pro], layout=layout_geo),
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

                html.Div([
                    html.H6("Technical & Soft Skills",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id="grpah-2",
                        figure={
                            'data': [skill_1, skill_2, skill_3
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                title = "",
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                width = 360,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.20,
                                  "y": -0.142606516291,
                                  "orientation": "h",
                                  'font' : dict(
                                    size=9,
                                    ),
                                },

                                xaxis=dict(
                                  autorange=True,
                                  showgrid=False,
                                  zeroline=True,
                                  showline=True,
                                  showticklabels=False
                                  ),
                                yaxis =
                                    dict(
                                        autorange=True,
                                        zeroline=True,
                                        showline=True,
                                        tickmode = 'array',
                                        tickvals = [10, 40, 90],
                                        ticktext = ['BEGINNER', 'GOOD', 'PRO'],
                                        showticklabels = True,
                                        tickfont = {'size' : 8}),
                                margin = {
                                  "r": 20,
                                  "t": 20,
                                  "b": 20,
                                  "l": 0
                                },
                                showlegend = True,
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 5

            html.Div([

                html.Div([
                    html.H6('Experiences',
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_resume))
                ], className="six columns"),

                html.Div([
                    html.H6("References & Recommendation Letter",
                            className="gs-header gs-table-header padded"),
                    html.Br([]),
                    html.P(children = [
                      html.Strong('Julien DAVAYAT - CWG2018 Project Director'), 
                    html.Br([]),
                    '+ 33 (0)6 87 73 76 63']),

                    html.P(children = [
                      html.Strong('Damien RIVOIRE - UEFA2016 Project Director'),
                      html.Br([]),
                      '+ 33 (0)6 33 64 38 17 ',
                      html.Br([]),
                      html.A(' Reference Letter', download = 'letter_euro2016.pdf', href = '/assets/letter_euro2016.pdf')]),

                    html.P(children = [
                      html.Strong('Adrien DEMENGEL - Operations Director'), 
                    html.Br([]),
                    '+ 33 (0)6 32 72 48 36 ', 
                    html.Br([]),
                    html.A(' Reference Letter', download = 'letter_projectmanager.pdf', href = '/assets/letter_projectmanager.pdf')]),

                    html.P(children = [
                      html.Strong('Muriel Renault - Zénith de Dijon'), 
                    html.Br([]),
                    'mrenault@zenith-dijon.fr',
                    html.Br([]),
                    html.A('Reference Letter', download = 'letter_zenithdijon.pdf', href = '/assets/letter_zenithdijon.pdf')]),


                ], className="six columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")


pricePerformance = html.Div([  # page 2

        print_button(),

        html.Div([
            Header(),

            # Row 2

            html.Div([

                html.Div([
                    html.H6("Professional Experiences",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-4',
                        figure = figure_hover,
                        config={
                            'displayModeBar': False
                        },
                        style = {'height' : '130px'}
                    )
                ], className="six columns"),

                html.Div([
                    html.H6("Main Informations",
                            className="gs-header gs-table-header padded"),
                    html.P(id = 'paragraphe-modify') 
                  ], className="six columns")

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Missions"], className="gs-header gs-table-header padded"),
                    html.P(children = ['text-brut'], id = 'text-mission', className="tiny-header", style = {'height' : '180'})
                ], className=" twelve columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6(["Skills Chart"], className="gs-header gs-table-header padded"),
                    dcc.Graph(id = 'soft_skill_graph', 
                    figure = figure_soft_skill,
                    className="tiny-header",
                    config={'displayModeBar': False},
                    style = {'height' : '200', 'margin-top': '10px'})
                ], className=" twelve columns"),

            ], className="row "),

            # Row 5

            html.Div([

            ], className="row "),

        ], className="subpage")

    ], className="page")


portfolioManagement = html.Div([ # page 3

        print_button(),

        html.Div([

            Header(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Portfolio"],
                            className="gs-header gs-table-header padded")
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Strong(["Stock style"]),
                    dcc.Graph(
                        id='graph-5',
                        figure={
                            'data': [
                                go.Scatter(
                                    x = ["1"],
                                    y = ["1"],
                                    hoverinfo = "none",
                                    marker = {
                                        "opacity": 0
                                    },
                                    mode = "markers",
                                    name = "B",
                                )
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                {
                                  "x": 0.990130093458,
                                  "y": 1.00181709504,
                                  "align": "left",
                                  "font": {
                                    "family": "Raleway",
                                    "size": 9
                                  },
                                  "showarrow": False,
                                  "text": "<b>Market<br>Cap</b>",
                                  "xref": "x",
                                  "yref": "y"
                                },
                                {
                                  "x": 1.00001816013,
                                  "y": 1.35907755794e-16,
                                  "font": {
                                    "family": "Raleway",
                                    "size": 9
                                  },
                                  "showarrow": False,
                                  "text": "<b>Style</b>",
                                  "xref": "x",
                                  "yanchor": "top",
                                  "yref": "y"
                                }
                              ],
                              autosize = False,
                              width = 200,
                              height = 150,
                              hovermode = "closest",
                              margin = {
                                "r": 30,
                                "t": 20,
                                "b": 20,
                                "l": 30
                              },
                              shapes = [
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rect",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "dash": "solid",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rect",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rect",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rect",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rect",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rect",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rect",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(255, 127, 14)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 1
                                  },
                                  "opacity": 0.9,
                                  "type": "rect",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rect",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                }
                              ],
                              xaxis = {
                                "autorange": True,
                                "range": [0.989694747864, 1.00064057995],
                                "showgrid": False,
                                "showline": False,
                                "showticklabels": False,
                                "title": "<br>",
                                "type": "linear",
                                "zeroline": False
                              },
                              yaxis = {
                                "autorange": True,
                                "range": [-0.0358637178721, 1.06395696354],
                                "showgrid": False,
                                "showline": False,
                                "showticklabels": False,
                                "title": "<br>",
                                "type": "linear",
                                "zeroline": False
                              }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )

                ], className="four columns"),

                html.Div([
                    html.P("Vanguard 500 Index Fund seeks to track the performance of\
                     a benchmark index that meaures the investment return of large-capitalization stocks."),
                    html.P("Learn more about this portfolio's investment strategy and policy.")
                ], className="eight columns middle-aligned"),

            ], className="row "),

            # Row 3

            html.Br([]),

            html.Div([

                html.Div([
                    html.H6(["Equity characteristics as of 01/31/2018"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_equity_char), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6(["Equity sector diversification"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_equity_diver), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")

feesMins = html.Div([  # page 4

        print_button(),

        html.Div([

            Header(),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Build a Data Pipeline - Example of Stock Exchange Data"],
                            className="gs-header gs-table-header padded"),

                    html.Br([]),

                    html.Div([

                        html.Div([
                            html.Strong(["Data Gathering"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.Strong(['Web']),
                            html.P(['Python Scraping : Requests / BeautifulSoup']),
                            html.P(['API : Postman / AlphaVantage']),
                            html.Strong(['DataBase']),
                            html.P(['SQL : - PostgreSQL / MySQL / SQLlite']),
                            html.Strong(['Local Files']),
                            html.P(['Excel, CSV, XLM, etc.']),
                                                                                    
                        ], className="nine columns")


                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["Data Wrangling"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.Strong(['Cleaning']),
                            html.P(['Jupyter Notebook : - Pandas, Numpy'])
                        ], className="nine columns")

                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["Data Visualisation"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.Strong(['Plotting']),
                            html.P(['Jupyter Notebook : - Matplotlib, Seaborn, Bokeh, Plotly'])
                        ], className="nine columns")

                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["Select your information"]),
                            html.P([]),
                            dcc.Dropdown(
                              id ='first-level-dropdown',
                              value = 'Graph',
                              options = [
                              {'label' : 'Code', 'value' : 'Code'},
                              {'label' : 'Graph', 'value' : 'Graph'}],
                              style = {'text-align' : 'left'}),
                            html.P([]),
                            dcc.Dropdown(
                              id = 'second-level-dropdown',
                              value = 'Plotly',
                              options = [
                              {'label' : 'Plotly', 'value' : 'Plotly'},
                              {'label' : 'Matplotlib', 'value' : 'Matplotlib'}],
                              style = {'text-align' : 'left'})
                        ], className="three columns right-aligned"),

                        html.Div(children = [
                          html.Img(id = 'python-code', src="https://i.ibb.co/B40CWPm/API-python-code.png", height='300', width='550'),
                          html.Img(id = 'sql-code', src="https://i.ibb.co/fDxmdpH/SQL-code.png", height='300', width='550'),
                          dcc.Graph(id = 'graph-7',
                              figure = dict(data = data_stock, layout = layout_stock),
                              config={
                            'displayModeBar': False
                            }),

                        ], className="nine columns", id = 'skill-display')

                    ], className="row ")

                ], className="twelve columns")

            ], className="row "),

        ], className="subpage")

    ], className="page")

distributions = html.Div([  # page 5

        print_button(),

        html.Div([

            Header(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Distributions"],
                            className="gs-header gs-table-header padded"),
                    html.Strong(["Distributions for this fund are scheduled quaterly"])
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Br([]),
                    html.H6(["Dividend and capital gains distributions"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_dividend), className="tiny-header")
                ], className="twelve columns"),

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Realized/unrealized gains as of 01/31/2018"], className="gs-header gs-table-header tiny-header")
                ], className=" twelve columns")

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.Table(make_dash_table(df_realized))
                ], className="six columns"),

                html.Div([
                    html.Table(make_dash_table(df_unrealized))
                ], className="six columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")

newsReviews = html.Div([  # page 6

        print_button(),

        html.Div([

            Header(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6('For Now',
                            className="gs-header gs-text-header padded"),
                    html.Br([]),
                    html.P("From my past experiences, I realized how much I was able to improve my own and my team's efficiency by providing us tools & KPI's. \
                        It all started from Excel, creating Operations Planning, Stock Monitoring, automatize administrative process and so on...", style = {'text-align' : 'justify'}),
                    html.Br([]),
                    html.P("Excel is good but you reach its limit easily. Then I thought to myself, what is the next move to take? What is the next software or computer language to learn ? What could lead me higher ? \
                    After a couple of days researching I discover Python and decided learning it, the hard way.", style = {'text-align' : 'justify'}),
                    html.Br([]),
                     html.P(children = [
                      "First days, weeks, months were hard, learning it from scratch, \
                      where new concepts and words pops up at every lines.It made the path bumpier than I thought it would be.\
                      However, I kept trying and I am convinced that the best way to learn is",
                      html.Strong(' learning by doing. '),
                      "Now this past few months are behind me, I finally got out the fog, and see clearly where I head to : Data Analysis & Business Intelligence"],
                      style = {'text-align' : 'justify'})
                ], className="six columns"),

                html.Div([
                    html.H6("And After ? ",
                            className="gs-header gs-table-header padded"),
                    html.Br([]),
                    html.P('What a wide new world that is ahead of me. The more I learnt, the more I realize there is to learn. \
                    Gathering data from whatever the source (web, excel, SGBD...) or the shape (Numbers, Text, Image, GeoLoc...). \
                    There is plenty of new technologies to use them, either BI tools (Microsoft BI / Tableau) to improve Business Decision-Making, \
                    or Tenserflow, Scikit-Learn for Data Science and make predictions, or Hadoop and/or Spark for Big Data Analysis'),
                    html.Br([]),
                    html.Strong('I feel like my journey is just starting')
                ], className="six columns"),

            ], className="row ")

        ], className="subpage")

    ], className="page")

noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")



# Describe the layout, or the UI, of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

app.config['suppress_callback_exceptions']=True
# Update page
# # # # # # # # #
# detail in depth what the callback below is doing
# # # # # # # # #
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/quentin-dumont' or pathname == '/quentin-dumont/overview':
        return overview
    elif pathname == '/quentin-dumont/professional-experience':
        return pricePerformance
    elif pathname == '/quentin-dumont/education':
        return portfolioManagement
    elif pathname == '/quentin-dumont/skills':
        return feesMins
    elif pathname == '/quentin-dumont/references':
        return distributions
    elif pathname == '/quentin-dumont/what-is-next':
        return newsReviews
    elif pathname == '/quentin-dumont/full-view' :
        return overview, pricePerformance, feesMins, newsReviews
    else:
        return noPage

@app.callback(
    Output('skill-display', 'children'),
    [Input('second-level-dropdown', 'value')])
def updatedisplay(value) :
  if value == 'SQL' :
    return html.Img(id = 'sql-code', src="https://i.ibb.co/fDxmdpH/SQL-code.png", height='300', width='550')
  elif value == 'Python' :
    return html.Img(id = 'python-code', src="https://i.ibb.co/B40CWPm/API-python-code.png", height='300', width='550')
  if value == 'Plotly' :
    return dcc.Graph(id = 'graph-7', figure = dict(data = data_stock, layout = layout_stock), config={'displayModeBar': False})
  if value == 'Matplotlib' :
    return html.Img(id = 'matplotlib-pic', src = 'https://i.ibb.co/D9Cb2nK/matplotlib.png', height = '300', width = '550')

text_zenith = html.Div([
  html.P('SALES & COMMUNICATION ASSISTANT'),
  html.Br([]),
  html.P('Zénith de Dijon'),
  html.P('2013 - 2014'),
  html.P('Dijon, France')
  ], style = dict(
    fontWeight = 'bold',
    fontSize = '140%',
    textAlign = 'center'))

mission_zenith = html.Div([
  html.P(children = [
    html.Strong('Business Development'),
    html.Br([]),
    'Commercial development of shows and private location.']),
  html.P(children = [
    html.Strong('Customer Relationship Management'),
    html.Br([]),
    'Customers research and loyalty management - partnerships creation.']),
  html.P(children = [
    html.Strong('Communication'),
    html.Br([]),
    'Participation in and monitoring of the communication/media plan of the Zénith.']),
  html.P(children = [
    html.Strong('Event Management'),
    html.Br([]),
  'Management of Private Events.'])
  ])

text_cwg2018 = html.Div([
  html.P(children = ['STOCK CONTROLLER',
  html.Br([]),
  'Commonwealth Games 2018']),
  html.P('GL events'),
  html.P('2017-2018'),
  html.P('Goald Coast, Australia')
  ], style = dict(
    fontWeight = 'bold',
    fontSize = '140%',
    textAlign = 'center'))

mission_cwg2018 = html.Div([
  html.P(children = [
    html.Strong('Tools & KPI’s development'),
    html.Br([]),
  'Development and implementation of a material stock monitoring \
  system to track and account all inbound and outbound material flows in the warehouse..']),
    html.P(children = [
    html.Strong('Logistics coordination'),
    html.Br([]),
    'Planning of stock distribution to each venue, \
    liaising with international logistic managers, cluster managers and site managers of each venue.']),
    html.P(children = [
    html.Strong('Risk Management'),
    html.Br([]),
    'Risk management: Optimization of logistics planning to ensure smooth material flows'])
  ])

text_euro2016 = html.Div([
  html.P(children = ['JUNIOR PROJECT MANAGER',
  html.Br([]),
  'UEFA EURO 2016' ]),
  html.P('GL events'),
  html.P('2015-2016'),
  html.P('Lyon, France')
  ], style = dict(
    fontWeight = 'bold',
    fontSize = '140%',
    textAlign = 'center'))

mission_euro2016 = html.Div([
  html.P(children = [
    html.Strong('Project Coordination'),
    html.Br([]),
    'Coordinate multiple projects (Budget 45 M €) and ensure full completion of scope of works.']),
  html.P(children = [
    html.Strong('Procurement'),
    html.Br([]),
    'Negotiate, analyse, and prepare purchase order, subcontracts, and cost control budgets over 30 + subcontractors.']),
  html.P(children = [
    html.Strong('Operations'),
    html.Br([]),
    'Plan and manage Plants & Equipment allocation during operations, reducing costs by 18 % - Budget 300 K €']),
  html.P(children = [
    html.Strong('Planning'),
    html.Br([]),
  'Planning resources in order to improve cost-allocation and time-efficiency.'])
  ])


text_baku2015 = html.Div([
  html.P(children = ['DOCUMENT CONTROLLER',
  html.Br([]),
  '1st European Games BAKU2015']),
  html.P('GL events'),
  html.P('2015'),
  html.P('Baku, Azerbaijan')
  ], style = dict(
    fontWeight = 'bold',
    fontSize = '140%',
    textAlign = 'center'))

mission_baku2015 = html.Div([
  html.P(children = [
    html.Strong('Financial Controlling'),
    html.Br([]),
    'Cost control and monitoring of expenses.']),
  html.P(children = [
    html.Strong('Change management'),
    html.Br([]),
    'Handling of additional requests and modifications from clients and integration in ongoing project workflows.']),
  html.P(children = [
    html.Strong('Project Administration'),
    html.Br([]),
    'Management of documents and communication with clients & stakeholders (e.g. H&S procedures, insurance and constructions permits)']),
  ])


text_mitry = html.Div([
  html.P('PROJECT MANAGER'),
  html.Br([]),
  html.P('GL events'),
  html.P('2017'),
  html.P('Paris, France')
  ], style = dict(
    fontWeight = 'bold',
    fontSize = '140%',
    textAlign = 'center'))

mission_mitry = html.Div([
  html.P(children = [
    html.Strong('Project Scoping'),
    html.Br([]),
    'Definition of project business cases & opportunities: manage and coordinate operations department. Analyse, define business opportunities and implement actions.']),
  html.P(children = [
    html.Strong('Project Planning'),
    html.Br([]),
    'Project planning & resource allocation: coordinate in-house team and subcontractors for presence on site. Define manpower, logistical schedule, materials need, and technical specificities.']),
  html.P(children = [
    html.Strong('Quality Management & Auditing'),
    html.Br([]),
    'Analysis and implementation of procedures and tools to improve project workflows and to take corrective actions. Automatize administrative tasks using Excel.']),
  html.P(children = [
    html.Strong('Reporting & Documentation'),
    html.Br([]),
    'Creation and maintenance of operational and financial reports and forecast alerts. Gather data and provide KPI’s to enable management to take actions.'])

  ])


text_tender = html.Div([
  html.P('BID MANAGER ASSISTANT'),
  html.Br([]),
  html.P('GL events'),
  html.P('2014'),
  html.P('Lyon, France')
  ], style = dict(
    fontWeight = 'bold',
    fontSize = '140%',
    textAlign = 'center'))

mission_tender = html.Div([
  html.P(children = [
    html.Strong('Bid Management'),
    html.Br([]),
    'Analysis of clients’ requirements and development of technical, administrative and financial solutions for international events (e.g. Rugby Worldcup England, Expo Milano, Pan Am Games Toronto).']),
  html.P(children = [
    html.Strong('Strategy Alignment'),
    html.Br([]),
    'trategy alignment: Evaluation of legal and financial possibilities and coordination between different departments (IT, Finance, Business Dvpt) regarding tender submission.']),
  
])


@app.callback(
  Output('second-level-dropdown', 'options'),
  [Input('first-level-dropdown', 'value')])
def updatedropdown(choice) :
  if choice == 'Graph' : 
    result = [
    {'label' : 'Matplotlib', 'value' : 'Matplotlib'},
    {'label' : 'Plotly', 'value' : 'Plotly'}]
    return result
  elif choice == 'Code' :
    result = [
    {'label' : 'Python', 'value' : 'Python'},
    {'label' : 'SQL', 'value' : 'SQL'}]
    return result

@app.callback(
    Output('paragraphe-modify', 'children'),
    [Input('graph-4', 'hoverData')])
def display_hover_data(hoverData):
  try : 
    if hoverData['points'][0]['text'] == 'Project Manager' :
      return text_mitry
    elif hoverData['points'][0]['text'] == 'Junior Project Manager' :
      return text_euro2016
    elif hoverData['points'][0]['text'] == 'Bid Manager Assistant' :
      return text_tender
    elif hoverData['points'][0]['text'] == 'Document Controller' :
      return text_baku2015
    elif hoverData['points'][0]['text'] == 'Stock Controller' :
      return text_cwg2018
    elif hoverData['points'][0]['text'] == 'Sales & Communications Assistant' :
      return text_zenith
  except :
      return text_cwg2018

@app.callback(
    Output('text-mission', 'children'),
    [Input('graph-4', 'hoverData')])
def display_hover_data(hoverData):
  try : 
    if hoverData['points'][0]['text'] == 'Sales & Communications Assistant' :
      return mission_zenith
    elif hoverData['points'][0]['text'] == 'Stock Controller' :
      return mission_cwg2018
    elif hoverData['points'][0]['text'] == 'Project Manager' :
      return mission_mitry
    elif hoverData['points'][0]['text'] == 'Junior Project Manager' :
      return mission_euro2016
    elif hoverData['points'][0]['text'] == 'Bid Manager Assistant' :
      return mission_tender
    elif hoverData['points'][0]['text'] == 'Document Controller' :
      return mission_baku2015
  except TypeError :
    return mission_cwg2018

@app.callback(
    Output('soft_skill_graph', 'figure'),
    [Input('graph-4', 'hoverData')])
def display_hover_data(hoverData):
  try : 
    if hoverData['points'][0]['text'] == 'Sales & Communications Assistant' :
      figure_soft_skill = {'data' : [chart_soft_skills_0], 'layout' : layout_soft_skills}
      return figure_soft_skill
    elif hoverData['points'][0]['text'] == 'Stock Controller' :
      figure_soft_skill = {'data' : [chart_soft_skills_5], 'layout' : layout_soft_skills}
      return figure_soft_skill
    elif hoverData['points'][0]['text'] == 'Project Manager' :
      figure_soft_skill = {'data' : [chart_soft_skills_4], 'layout' : layout_soft_skills}
      return figure_soft_skill
    elif hoverData['points'][0]['text'] == 'Junior Project Manager' :
      figure_soft_skill = {'data' : [chart_soft_skills_3], 'layout' : layout_soft_skills}
      return figure_soft_skill
    elif hoverData['points'][0]['text'] == 'Bid Manager Assistant' :
      figure_soft_skill = {'data' : [chart_soft_skills_1], 'layout' : layout_soft_skills}
      return figure_soft_skill
    elif hoverData['points'][0]['text'] == 'Document Controller' :
      figure_soft_skill = {'data' : [chart_soft_skills_2], 'layout' : layout_soft_skills}
      return figure_soft_skill
  except TypeError :
      figure_soft_skill = {'data' : [chart_soft_skills_5], 'layout' : layout_soft_skills}
      return figure_soft_skill

# # # # # # # # #
# detail the way that external_css and external_js work and link to alternative method locally hosted
# # # # # # # # #
external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.run_server(debug=True)
