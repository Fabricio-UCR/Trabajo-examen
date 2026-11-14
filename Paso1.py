def cargar_sensores_unicos(
    ruta_txt: str
) -> set[tuple[str, str, float, str]]:

    lecturas = set()

    with open(ruta_txt, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            limpia = linea.strip()

            if limpia and not limpia.startswith("#"):
                partes = [p.strip() for p in limpia.split("|")]

                maquina = partes[0]

                sensor, str_val = partes[1].split(":")
                sensor = sensor.strip()
                metrica = float(str_val.strip())

                estado = partes[2].upper()

                registro = (maquina, sensor, metrica, estado)

                lecturas.add(registro)

    return lecturas
