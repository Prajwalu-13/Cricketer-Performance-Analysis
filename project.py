import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import tkinter
from tkinter import *
from PIL import ImageTk, Image

data = pd.read_csv("vk.csv")
def run_scored_total():
    matches = data.index
    figure = px.line(data, x=matches, y="Runs", 
                    title='Runs Scored by Virat Kohli Between 18-Aug-08 - 22-Jan-17')
    figure.show()

# Batting Positions
def batting_positions_matches():
    data["Pos"] = data["Pos"].map({3.0: "Batting At 3", 4.0: "Batting At 4", 2.0: "Batting At 2", 
                                1.0: "Batting At 1", 7.0:"Batting At 7", 5.0:"Batting At 5", 
                                6.0: "batting At 6"})

    Pos = data["Pos"].value_counts()
    label = Pos.index
    counts = Pos.values
    colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

    fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
    fig.update_layout(title_text='Number of Matches At Different Batting Positions')
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                    marker=dict(colors=colors, line=dict(color='black', width=3)))
    fig.show()

def batting_positions_runs():
    label = data["Pos"]
    counts = data["Runs"]
    colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

    fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
    fig.update_layout(title_text='Runs By Virat Kohli At Different Batting Positions')
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                    marker=dict(colors=colors, line=dict(color='black', width=3)))
    fig.show()

def centuriesn():
    centuries = data.query("Runs >= 100")
    figure = px.bar(centuries, x=centuries["Inns"], y = centuries["Runs"], 
                    color = centuries["Runs"],
                    title="Centuries By Virat Kohli in First Innings Vs. Second Innings")
    figure.show()

def dismissal():
    dismissal = data["Dismissal"].value_counts()
    label = dismissal.index
    counts = dismissal.values
    colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

    fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
    fig.update_layout(title_text='Dismissals of Virat Kohli')
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                    marker=dict(colors=colors, line=dict(color='black', width=3)))
    fig.show()

def runs_against_opposition():
    figure = px.bar(data, x=data["Opposition"], y = data["Runs"], color = data["Runs"],
                title="Most Runs Against Teams")
    figure.show()

def centuries_against_opposition():
    centuries = data.query("Runs >= 100")
    figure = px.bar(centuries, x=centuries["Opposition"], y = centuries["Runs"], 
                    color = centuries["Runs"],
                    title="Most Centuries Against Teams")
    figure.show()

top = tkinter.Tk()
top.title("                 Mini Project            ")
top.geometry('600x600')
frame = Frame( width=300, height=450)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("cri.jpeg"))
label = Label(frame, image = img)
label.pack()

A = tkinter.Label(top, text="Cricketer - Virat Kohli Analysis",font=("Helvetica", 20)).grid(row=1, column=0, pady = (15,15), padx = (30,30))
B = tkinter.Button(top, text ="run_scored_total", command=run_scored_total, font=("Helvetica",10)).grid(row=2, column=0, pady = (15,15), padx = (30,30))
C = tkinter.Button(top, text ="batting_positions_matches",command=batting_positions_matches, font=("Helvetica",10)).grid(row=3, column=0, pady = (0,15), padx = (30,30))
D = tkinter.Button(top, text ="batting_positions_runs",command=batting_positions_runs, font=("Helvetica",10)).grid(row=4, column=0, pady = (0,15), padx = (30,30))
E = tkinter.Button(top, text ="centuries",command=centuriesn, font=("Helvetica",10)).grid(row=5, column=0, pady = (0,15), padx = (30,30))
F = tkinter.Button(top, text ="dismissal",command=dismissal, font=("Helvetica",10)).grid(row=6, column=0, pady = (0,15), padx = (30,30))
G = tkinter.Button(top, text ="runs_against_opposition",command=runs_against_opposition, font=("Helvetica",10)).grid(row=7, column=0, pady = (0,15), padx = (30,30))
H = tkinter.Button(top, text ="centuries_against_opposition",command=centuries_against_opposition, font=("Helvetica",10)).grid(row=8, column=0, pady = (0,15), padx = (30,30))
top.mainloop()
data = pd.read_csv("vk.csv")
# print(data.head())

# print(data.isnull().sum())

# data["Runs"].sum()

# strike_rate = data.query("SR >= 120")
# print(strike_rate)