from pathlib import Path
from analitica import (
    consolidar_totales_por_producto,
    filtrar_alertas_criticas,
    maquinas_con_alertas,
    ranking_productos,
)
from procesamiento_datos import (
    cargar_lotes_csv,
    cargar_sensores_unicos,
)


def main() -> None:
    # Soporta ejecucion tanto desde la raiz del proyecto como desde la subcarpeta
    base_dir = Path(__file__).resolve().parent.parent if Path(__file__).resolve().parent.name == "solucion" else Path(__file__).resolve().parent
    ruta_sensores = base_dir / "data" / "bitacora_sensores.txt"
    ruta_lotes = base_dir / "data" / "lotes_produccion.csv"

    print("=" * 70)
    print("SISTEMA DE GESTIÓN Y ANALÍTICA DE PLANTA INDUSTRIAL - II-1119")
    print("=" * 70)

    # 1. Carga TXT
    lecturas = cargar_sensores_unicos(str(ruta_sensores))
    print(f"\n1. Lecturas únicas procesadas (Set): {len(lecturas)}")

    # 2. Carga CSV
    lotes = cargar_lotes_csv(str(ruta_lotes))
    print(f"2. Lotes válidos y saneados (CSV - EAFP): {len(lotes)}")

    # 3. Filtrado con Comprensión de Listas
    alertas_criticas = filtrar_alertas_criticas(lecturas)
    print(f"3. Alertas críticas detectadas: {len(alertas_criticas)}")

    # 4. Operaciones de Conjuntos (Sets)
    maquinas_riesgo = maquinas_con_alertas(lecturas)
    todas_maquinas = {maq for maq, _, _, _ in lecturas}
    print(f"4. Máquinas con incidencias: {sorted(maquinas_riesgo)}")
    print(f"   Máquinas operando óptimas: {sorted(todas_maquinas - maquinas_riesgo)}")

    # 5. Agrupación en Diccionarios
    resumen = consolidar_totales_por_producto(lotes)
    print("5. Consolidación de producción completada:")
    for prod, datos in resumen.items():
        print(f"   • {prod:<22} -> Unidades: {datos['cantidad_total']:>5} | Total: ${datos['costo_total']:>9.2f}")

    # 6. Slicing y Ranking
    podio = ranking_productos(resumen, top_n=3)
    print("6. Podio Top 3 de Inversión (Slicing):")
    for pos, (prod, inversion) in enumerate(podio, start=1):
        print(f"   #{pos}: {prod:<22} ${inversion:>9.2f}")

    print("\n" + "=" * 70)
    print("¡Procesamiento finalizado exitosamente!")
    print("=" * 70)


if __name__ == "__main__":
    main()
