import base64
from typing import Tuple, Dict
import networkx as nx
from rdkit import Chem
from rdkit.Chem import Draw, AllChem
from rdkit.Chem.Draw import rdMolDraw2D


def smi2mol(smi: str, include_h: bool = True) -> Chem.Mol:
    m = Chem.MolFromSmiles(Chem.MolToSmiles(Chem.MolFromSmiles(smi)))
    if include_h:
        return Chem.AddHs(m)
    return m


def mol_svg_b64(m: Chem.Mol, size: Tuple[int, int] = (350, 350)) -> str:
    d2d = rdMolDraw2D.MolDraw2DSVG(350, 300)
    d2d.drawOptions().addAtomIndices = True
    d2d.drawOptions().addStereoAnnotation = True
    d2d.DrawMolecule(m)
    d2d.FinishDrawing()
    encoded = base64.b64encode(d2d.GetDrawingText().encode())
    return f"data:image/svg+xml;base64,{encoded.decode()}"


def mol_coords(m: Chem.Mol):
    AllChem.Compute2DCoords(m)
    c = m.GetConformer()
    return c.GetPositions()


def mol2nx(m: Chem.Mol) -> nx.Graph:
    pos = mol_coords(m)
    G = nx.Graph()
    for a in m.GetAtoms():
        G.add_node(
            a.GetIdx(),
            atomic_sym=a.GetSymbol(),
            x=pos[a.GetIdx()][0],
            y=pos[a.GetIdx()][1],
        )
    for b in m.GetBonds():
        G.add_edge(b.GetBeginAtom().GetIdx(), b.GetEndAtom().GetIdx())
    return G


def nx2cy(G: nx.Graph) -> Dict:
    cy = nx.readwrite.json_graph.cytoscape_data(G)
    for idx, n in enumerate(cy["elements"]["nodes"]):
        n["position"] = {
            "x": 100 * n["data"]["x"],
            "y": 100 * n["data"]["y"],
        }
        n["data"]["label"] = n["data"]["atomic_sym"] + ":" + n["data"]["id"]
        n["data"]["index"] = "-1"
        n["classes"] = "unselected"
    return cy


def smi2cy(smi: str) -> Dict:
    m = smi2mol(smi)
    G = mol2nx(m)
    return nx2cy(G)
