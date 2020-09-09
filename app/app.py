# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import base64
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
import plotly.express as px
from dash.dependencies import Input, Output, State, ALL
from copy import deepcopy

from app import utils

# Load extra layouts
cyto.load_extra_layouts()

# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
external_stylesheets = []
ERROR_SVG = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' height='350' width='350'%3E%3Ctext x='0' y='15' fill='red'%3ECould not parse SMILES!%3C/text%3E%3C/svg%3E"
INSTRUCTIONS = """### Instructions
1. Paste in a SMILES string
2. Selected the atoms *in order while holding SHIFT* according to your mapping and see the translation from RDKit standard numbering to your own selected mapping.

You can deselect the mapping by clicking in the blank canvas.
"""
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        dcc.Store(id="mol-container"),
        html.H1(children="Hello NP-MRD"),
        html.Div(
            children=[
                html.Code("atom_order_app"),
                " A web application for mapping atom order",
            ]
        ),
        dcc.Markdown(children=INSTRUCTIONS),
        html.Br(),
        html.Div(
            [
                "SMILES: ",
                dcc.Input(id="smi-input", value="c1ccccc1", type="text"),
                # dcc.Checklist(
                #     id="include-h-input",
                #     options=[{"label": "Include H?", "value": "true"}],
                #     value=["true"],
                # ),
            ]
        ),
        html.Br(),
        html.Img(id="smi-output", src=""),
        cyto.Cytoscape(
            id="mol-cyto",
            # responsive=True,
            layout={"name": "preset"},
            # layout={"name": "cola"},
            style={"width": "80%", "height": "500px", "border-style": "solid"},
            elements=[],
            stylesheet=[
                # Group selectors
                {
                    "selector": "node",
                    "style": {
                        "content": "data(label)",
                        "text-halign": "center",
                        "text-valign": "center",
                        "width": "label*2",
                        "height": "label*2",
                        "color": "index",
                    },
                },
                {"selector": ".selected", "style": {"color": "red",}},
            ],
        ),
        html.H4(children="Atom Mapping"),
        html.Div(id="atom-output", children=""),
    ]
)


@app.callback(
    [Output("smi-output", "src"), Output("mol-cyto", "elements"),],
    [
        Input(component_id="smi-input", component_property="value"),
        # Input(component_id="include-h-input", component_property="value"),
    ],
)
def update_mol_cyto(smi):
    # Parse input smiles and return SVG image
    # Returns error message if fails.
    try:
        svg = utils.mol_svg_b64(utils.smi2mol(smi))
        cy = utils.smi2cy(smi)["elements"]
        # print(cy)
        return svg, cy
    except TypeError:
        return ERROR_SVG, []


@app.callback(
    Output("atom-output", "children"),
    [Input("mol-cyto", "elements"), Input("mol-cyto", "selectedNodeData")],
)
def update_atom_text(cy, selected):
    if not selected:
        selected = []
    print("selected", selected)
    return create_mol_table(cy, selected=selected)


def create_mol_table(cy, selected=[]):
    last_index = 0
    data = []
    indices = {n["data"]["id"]: n["data"]["index"] for n in cy["nodes"]}
    for s in selected:
        indices[s["id"]] = last_index
        last_index += 1
    for idx, n in enumerate(cy["nodes"]):
        data.append(
            f"{n['data']['atomic_sym']}:{n['data']['id']} -> {indices[n['data']['id']]}"
        )
    return dcc.Markdown(" - " + "\n - ".join(data)) if data else ""
