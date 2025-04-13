from io import StringIO
from typing import List

import pandas as pd

import data.isotope
from exceptions import IsotopeNotFound, HistoryNotFound
import matplotlib.pyplot as plt

from model.HistoryDeleteRequest import HistoryDeleteRequest
from model.HistoryRequest import HistoryRequest
from model.HistoryResponse import HistoryResponse
from model.IsotopeResponse import IsotopeResponse
from data.history_db import save, update, get_history_by_id, get_history_by_isotope_number, get_histories, delete


def get_isotope_by_number(isotope_number):
    res = data.isotope.get_isotope_by_number(isotope_number)
    if res.empty:
        raise IsotopeNotFound(isotope_number)
    return df_to_isotope_response(res)

def get_isotopes():
    res = data.isotope.get_isotopes().apply(df_to_isotope_response, axis=1)
    return res

def save_history(isotope_number: int):
    history = get_history_by_isotope_number(isotope_number)
    if history: update(HistoryRequest(isotope_number=isotope_number))
    else: save(HistoryRequest(isotope_number=isotope_number))

def delete_history(history: HistoryDeleteRequest):
    if not get_history_by_id(history.history_id):
        raise HistoryNotFound(history.history_id)
    delete(history)

def get_history() -> List[HistoryResponse]:
    histories = get_histories()
    return list(map(lambda x: HistoryResponse(history_id=x['history_id'], isotope_number=x['isotope_number'], seen_at=x['seen_at']), histories))

def df_to_isotope_response(s: pd.Series):
    s = s[s != 0]
    masses = s[s.index.str.startswith(('mass', 'percentage'))].values
    mass_dict = {}

    for i in range(0, len(masses), 2):
        try:
            mass_dict[int(masses[i])] = float(masses[i + 1])
        except IndexError:
            continue

    response = IsotopeResponse(
        number=int(s["number"]),
        symbol=s["symbol"],
        name=s["name"],
        mass=mass_dict,
        weight=float(s["weight"]),
        svg_data=""
    )
    return response

def visualize_isotope_percentage_by_number(isotope_number):
    res = get_isotope_by_number(isotope_number)
    plt.bar(x=res.mass.keys(), height=res.mass.values())
    plt.xticks(ticks=list(res.mass.keys()), labels=list(res.mass.keys()))
    svg_buffer = StringIO()
    plt.savefig(svg_buffer, format='svg')
    plt.close()
    svg_data = svg_buffer.getvalue()
    res.add_svg_data(svg_data)
    return res

