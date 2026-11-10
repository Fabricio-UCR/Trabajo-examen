#paso 2
import csv
from typing import Any


def cargar_lotes_csv(ruta_csv: str) -> list[dict[str, Any]]:
    lotes_validos: list[dict[str, Any]] = []

    with open(ruta_csv, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                id_lote = fila["id_lote"].strip()
                producto = fila["producto"].strip().title()
                estado = fila["estado"].strip().upper()
                cantidad = int(fila["cantidad"].strip())
                costo_unitario = float(fila["costo_unitario"].strip())

                if cantidad <= 0:
                    continue  

                lote: dict[str, Any] = {
                    "id_lote": id_lote,
                    "producto": producto,
                    "cantidad": cantidad,
                    "costo_unitario": costo_unitario,
                    "estado": estado,
                }
                lotes_validos.append(lote)
            except (ValueError, KeyError, AttributeError):
                continue 

    return lotes_validos
