import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from sklearn import datasets
from sklearn.cluster import KMeans
from glob import glob
from os import getcwd, chdir
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow import keras
import numpy as np  
import json
algo_list = glob('*.h5')
print(algo_list)


#importing word index
with open('word_index.json') as f:
    word_index = json.load(f)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("Pilih algoritma"),
                dcc.Dropdown(
                    id="algo",
                    options=[
                        {"label": algo, "value": algo} for algo in algo_list
                    ],
                    value="2-Layer-Bidirectional-LTSM.h5",
                ),
            ]
        ),

        dbc.FormGroup(
            [
                dbc.Label("Perkataan benih"),
                dbc.Input(id="seed",value="Cinta"),
            ]
        ),
        
        dbc.FormGroup(
            [
                dbc.Label("Panjang perkataan"),
                dbc.Input(id="word-length", type="number", value=10),
            ]
        ),

        dbc.FormGroup(
            [
            dbc.Button("Cipta", id="example-button", className="mr-2")
            ]
        ),
    ],
    body=True,
)

app.layout = dbc.Container(
    [
        html.H1("AI Cipta"),
        html.H1("Cipta Lirik Lagu"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dbc.Jumbotron(id="algo-output",
                    ), md=8, 
                ),               
            ],
            align="center",
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("algo-output", "children"),
    [
        dash.dependencies.Input("example-button",'n_clicks'),
        dash.dependencies.State("word-length", "value"),
        dash.dependencies.State("algo", "value"),
        dash.dependencies.State("seed", "value"),
        
    ],
)

def update_output_div(value,length,algo,seed):
    #importing saved model
    model = keras.models.load_model(algo)
    seed_text = seed
    next_words = length
    max_sequence_len = 100
    tokenizer = Tokenizer()
    tokenizer.word_index = word_index
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        # print(token_list)
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)