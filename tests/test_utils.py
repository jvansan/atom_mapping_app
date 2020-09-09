import pytest
from app.utils import *
from rdkit import Chem

def test_smi2mol():
    m = smi2mol("c1ccccc1", include_h=False)
    assert Chem.MolToSmiles(m) == "c1ccccc1"

def test_smi2mol_include_h():
    m = smi2mol("c1ccccc1", include_h=True)
    assert Chem.MolToSmiles(m) == "[H]c1c([H])c([H])c([H])c([H])c1[H]"


def test_smi2mol_bad_smi():
    # TypeError is base of Python.Boost.ArgumentError
    with pytest.raises(TypeError):
        m = smi2mol("c")


def test_mol_svg_b64():
    m = smi2mol("C", include_h=True)
    svg = mol_svg_b64(m)
    assert svg == "data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0nMS4wJyBlbmNvZGluZz0naXNvLTg4NTktMSc/Pgo8c3ZnIHZlcnNpb249JzEuMScgYmFzZVByb2ZpbGU9J2Z1bGwnCiAgICAgICAgICAgICAgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJwogICAgICAgICAgICAgICAgICAgICAgeG1sbnM6cmRraXQ9J2h0dHA6Ly93d3cucmRraXQub3JnL3htbCcKICAgICAgICAgICAgICAgICAgICAgIHhtbG5zOnhsaW5rPSdodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rJwogICAgICAgICAgICAgICAgICB4bWw6c3BhY2U9J3ByZXNlcnZlJwp3aWR0aD0nMzUwcHgnIGhlaWdodD0nMzAwcHgnIHZpZXdCb3g9JzAgMCAzNTAgMzAwJz4KPCEtLSBFTkQgT0YgSEVBREVSIC0tPgo8cmVjdCBzdHlsZT0nb3BhY2l0eToxLjA7ZmlsbDojRkZGRkZGO3N0cm9rZTpub25lJyB3aWR0aD0nMzUwJyBoZWlnaHQ9JzMwMCcgeD0nMCcgeT0nMCc+IDwvcmVjdD4KPHBhdGggY2xhc3M9J2JvbmQtMCcgZD0nTSAxNzUsMTUwIEwgMjU0LjQ4OCwxNTAnIHN0eWxlPSdmaWxsOm5vbmU7ZmlsbC1ydWxlOmV2ZW5vZGQ7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjJweDtzdHJva2UtbGluZWNhcDpidXR0O3N0cm9rZS1saW5lam9pbjptaXRlcjtzdHJva2Utb3BhY2l0eToxJyAvPgo8cGF0aCBjbGFzcz0nYm9uZC0xJyBkPSdNIDE3NSwxNTAgTCA5NS41MTIyLDE1MCcgc3R5bGU9J2ZpbGw6bm9uZTtmaWxsLXJ1bGU6ZXZlbm9kZDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MnB4O3N0cm9rZS1saW5lY2FwOmJ1dHQ7c3Ryb2tlLWxpbmVqb2luOm1pdGVyO3N0cm9rZS1vcGFjaXR5OjEnIC8+CjxwYXRoIGNsYXNzPSdib25kLTInIGQ9J00gMTc1LDE1MCBMIDE3NSw3Mi41NzU3JyBzdHlsZT0nZmlsbDpub25lO2ZpbGwtcnVsZTpldmVub2RkO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDoycHg7c3Ryb2tlLWxpbmVjYXA6YnV0dDtzdHJva2UtbGluZWpvaW46bWl0ZXI7c3Ryb2tlLW9wYWNpdHk6MScgLz4KPHBhdGggY2xhc3M9J2JvbmQtMycgZD0nTSAxNzUsMTUwIEwgMTc1LDIyNy40MjQnIHN0eWxlPSdmaWxsOm5vbmU7ZmlsbC1ydWxlOmV2ZW5vZGQ7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjJweDtzdHJva2UtbGluZWNhcDpidXR0O3N0cm9rZS1saW5lam9pbjptaXRlcjtzdHJva2Utb3BhY2l0eToxJyAvPgo8dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9InN0YXJ0IiB4PScyNTcuNTg1JyB5PScxNTQuNjQ1JyBzdHlsZT0nZm9udC1zaXplOjMwcHg7Zm9udC1zdHlsZTpub3JtYWw7Zm9udC13ZWlnaHQ6bm9ybWFsO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lO2ZvbnQtZmFtaWx5OnNhbnMtc2VyaWY7ZmlsbDojMDAwMDAwJyA+PHRzcGFuPkg8L3RzcGFuPjwvdGV4dD4KPHRleHQgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiIHRleHQtYW5jaG9yPSJlbmQiIHg9JzkyLjQxNTMnIHk9JzE1NC42NDUnIHN0eWxlPSdmb250LXNpemU6MzBweDtmb250LXN0eWxlOm5vcm1hbDtmb250LXdlaWdodDpub3JtYWw7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOm5vbmU7Zm9udC1mYW1pbHk6c2Fucy1zZXJpZjtmaWxsOiMwMDAwMDAnID48dHNwYW4+SDwvdHNwYW4+PC90ZXh0Pgo8dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9InN0YXJ0IiB4PScxNjQuNjc2JyB5PSc2MS43MzYyJyBzdHlsZT0nZm9udC1zaXplOjMwcHg7Zm9udC1zdHlsZTpub3JtYWw7Zm9udC13ZWlnaHQ6bm9ybWFsO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lO2ZvbnQtZmFtaWx5OnNhbnMtc2VyaWY7ZmlsbDojMDAwMDAwJyA+PHRzcGFuPkg8L3RzcGFuPjwvdGV4dD4KPHRleHQgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiIHRleHQtYW5jaG9yPSJzdGFydCIgeD0nMTY0LjY3NicgeT0nMjQ3LjU1NScgc3R5bGU9J2ZvbnQtc2l6ZTozMHB4O2ZvbnQtc3R5bGU6bm9ybWFsO2ZvbnQtd2VpZ2h0Om5vcm1hbDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6bm9uZTtmb250LWZhbWlseTpzYW5zLXNlcmlmO2ZpbGw6IzAwMDAwMCcgPjx0c3Bhbj5IPC90c3Bhbj48L3RleHQ+Cjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PScxOTYuODk5JyB5PScxMzEuNTg1JyBzdHlsZT0nZm9udC1zaXplOjIzcHg7Zm9udC1zdHlsZTpub3JtYWw7Zm9udC13ZWlnaHQ6bm9ybWFsO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lO2ZvbnQtZmFtaWx5OnNhbnMtc2VyaWY7ZmlsbDojMDAwMDAwJyA+PHRzcGFuPjA8L3RzcGFuPjwvdGV4dD4KPHRleHQgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9JzI5OC44NzknIHk9JzE1My40ODQnIHN0eWxlPSdmb250LXNpemU6MjNweDtmb250LXN0eWxlOm5vcm1hbDtmb250LXdlaWdodDpub3JtYWw7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOm5vbmU7Zm9udC1mYW1pbHk6c2Fucy1zZXJpZjtmaWxsOiMwMDAwMDAnID48dHNwYW4+MTwvdHNwYW4+PC90ZXh0Pgo8dGV4dCBkb21pbmFudC1iYXNlbGluZT0iY2VudHJhbCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0nNTEuMTIxJyB5PScxNTMuNDg0JyBzdHlsZT0nZm9udC1zaXplOjIzcHg7Zm9udC1zdHlsZTpub3JtYWw7Zm9udC13ZWlnaHQ6bm9ybWFsO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTpub25lO2ZvbnQtZmFtaWx5OnNhbnMtc2VyaWY7ZmlsbDojMDAwMDAwJyA+PHRzcGFuPjI8L3RzcGFuPjwvdGV4dD4KPHRleHQgZG9taW5hbnQtYmFzZWxpbmU9ImNlbnRyYWwiIHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9JzE3NScgeT0nMjkuNjA1MScgc3R5bGU9J2ZvbnQtc2l6ZToyM3B4O2ZvbnQtc3R5bGU6bm9ybWFsO2ZvbnQtd2VpZ2h0Om5vcm1hbDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6bm9uZTtmb250LWZhbWlseTpzYW5zLXNlcmlmO2ZpbGw6IzAwMDAwMCcgPjx0c3Bhbj4zPC90c3Bhbj48L3RleHQ+Cjx0ZXh0IGRvbWluYW50LWJhc2VsaW5lPSJjZW50cmFsIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PScxNzUnIHk9JzI3Ny4zNjMnIHN0eWxlPSdmb250LXNpemU6MjNweDtmb250LXN0eWxlOm5vcm1hbDtmb250LXdlaWdodDpub3JtYWw7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOm5vbmU7Zm9udC1mYW1pbHk6c2Fucy1zZXJpZjtmaWxsOiMwMDAwMDAnID48dHNwYW4+NDwvdHNwYW4+PC90ZXh0Pgo8L3N2Zz4K"


def test_mol2nx():
    m = smi2mol("C", include_h=True)
    G = mol2nx(m)
    assert len(G.nodes) == 5


def test_nx2cy():
    m = smi2mol("C", include_h=True)
    G = mol2nx(m)
    cy = nx2cy(G)
    assert cy["data"] == []
    assert len(cy ["elements"]["nodes"]) == 5