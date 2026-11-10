#paso 4
def maquinas_con_alertas(todas_lecturas:set[tuple[str, str, float, str]]) -> set[str]:
    return {maquina for maquina, _ , _. estado in todas_lecturas if estado !="NORMAL"}
