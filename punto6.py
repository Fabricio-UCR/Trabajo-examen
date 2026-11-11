def ranking_productos(
    resumen: dict[str, dict[str, float]], top_n: int = 3
) -> list[tuple[str, float]]:
    lista_items: list[tuple[str, float]] = [
        (prod, datos["costo_total"]) for prod, datos in resumen.items()
    ]
    ordenados = sorted(lista_items, key=lambda item: item[1], reverse=True)
    return ordenados[:top_n]
