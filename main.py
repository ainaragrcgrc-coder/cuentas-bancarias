from controller.cuenta_controller import CuentaController


def main():
    print("========================================")
    print("       SISTEMA DE CUENTAS BANCARIAS")
    print("========================================")

    controller = CuentaController()

    # ========================================
    # CUENTA BASE
    # ========================================

    print("\n--- CUENTA BASE ---")

    controller.crear_cuenta(
        "001",
        "base",
        15000,
        0.12
    )

    controller.consignar("001", 2000)
    controller.retirar("001", 1000)

    cuenta = controller.obtener_cuenta("001")
    cuenta.calcular_interes_mensual()

    print(controller.mostrar_cuenta("001"))

    # ========================================
    # CUENTA DE AHORROS
    # ========================================

    print("\n--- CUENTA DE AHORROS ---")

    controller.crear_cuenta(
        "002",
        "ahorros",
        15000,
        0.12
    )

    cuenta_ahorros = controller.obtener_cuenta("002")

    print(f"Cuenta activa: {cuenta_ahorros.activa}")

    controller.consignar("002", 2000)
    controller.retirar("002", 1000)
    controller.realizar_extracto_mensual("002")

    print(controller.mostrar_cuenta("002"))

    print(f"Cuenta activa: {cuenta_ahorros.activa}")

    # ========================================
    # CUENTA CORRIENTE
    # ========================================

    print("\n--- CUENTA CORRIENTE ---")

    controller.crear_cuenta(
        "003",
        "corriente",
        1000,
        0.12
    )

    controller.retirar("003", 1500)

    print("Después del retiro de 1.500 €:")
    print(controller.mostrar_cuenta("003"))

    controller.consignar("003", 300)

    print("\nDespués de consignar 300 €:")
    print(controller.mostrar_cuenta("003"))

    controller.consignar("003", 500)

    print("\nDespués de consignar 500 €:")
    print(controller.mostrar_cuenta("003"))


if __name__ == "__main__":
    main()
    