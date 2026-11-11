def consolidar_totales_por_producto(
    lotes: list[dict[str, Any]],
) -> dict[str, dict[str, float]]:
    resumen: dict[str, dict[str, float]] = {}
    for lote in lotes:
        if lote["estado"] != "COMPLETADO":
            continue

        prod = lote["producto"]
        cant = lote["cantidad"]
        inversion = cant * lote["costo_unitario"]

        if prod not in resumen:
            resumen[prod] = {"cantidad_total": 0, "costo_total": 0.0}

        resumen[prod]["cantidad_total"] += cant
        resumen[prod]["costo_total"] += inversion

    return resumen
