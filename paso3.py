def filtrar_alertas_criticas(
    lecturas: set[tuple[str, str, float, str]]
) -> list[tuple[str, str, float]]:

    return [
        (maq, sensor, valor)
        for maq, sensor, valor, estado in lecturas
        if estado == "CRITICO"
    ]
