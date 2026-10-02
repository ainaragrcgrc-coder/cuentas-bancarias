from controller.cuenta_controller import CuentaController


print("========================================")
print("       PRUEBAS DEL CONTROLLER")
print("========================================")


# ========================================
# CREAR CONTROLLER
# ========================================

controller = CuentaController()


# ========================================
# PRUEBA 1 - CUENTA BASE
# ========================================

print("\n--- PRUEBA 1: CUENTA BASE ---")

controller.crear_cuenta(
    "001",
    "base",
    10000,
    0.12
)

controller.consignar("001", 2000)
controller.retirar("001", 1000)

print(controller.mostrar_cuenta("001"))


# ========================================
# PRUEBA 2 - CUENTA DE AHORROS
# ========================================

print("\n--- PRUEBA 2: CUENTA DE AHORROS ---")

controller.crear_cuenta(
    "002",
    "ahorros",
    12000,
    0.12
)

ahorros = controller.obtener_cuenta("002")

print(f"Estado inicial: {ahorros.activa}")

controller.retirar("002", 3000)

print(controller.mostrar_cuenta("002"))
print(f"Estado después del retiro: {ahorros.activa}")


# ========================================
# PRUEBA 3 - CUENTA INACTIVA
# ========================================

print("\n--- PRUEBA 3: CUENTA INACTIVA ---")

controller.crear_cuenta(
    "003",
    "ahorros",
    12000,
    0.12
)

controller.retirar("003", 3000)

try:
    controller.retirar("003", 1000)
except ValueError as error:
    print(f"Error esperado: {error}")


# ========================================
# PRUEBA 4 - MÁS DE 4 RETIROS
# ========================================

print("\n--- PRUEBA 4: COMISIÓN POR RETIROS ---")

controller.crear_cuenta(
    "004",
    "ahorros",
    20000,
    0.12
)

for i in range(5):
    controller.retirar("004", 100)

controller.realizar_extracto_mensual("004")

ahorros = controller.obtener_cuenta("004")

print(f"Retiros realizados: {ahorros._numero_retiros}")
print(f"Comisión mensual: ${ahorros._comision_mensual:.2f}")
print(f"Saldo final: ${ahorros._saldo:.2f}")


# ========================================
# PRUEBA 5 - SOBREGIRO
# ========================================

print("\n--- PRUEBA 5: SOBREGIRO ---")

controller.crear_cuenta(
    "005",
    "corriente",
    1000,
    0.12
)

controller.retirar("005", 1500)

corriente = controller.obtener_cuenta("005")

print(f"Saldo: ${corriente._saldo:.2f}")
print(f"Sobregiro: ${corriente._sobregiro:.2f}")


# ========================================
# PRUEBA 6 - CANCELAR SOBREGIRO
# ========================================

print("\n--- PRUEBA 6: CANCELAR SOBREGIRO ---")

controller.consignar("005", 300)

print(f"Saldo: ${corriente._saldo:.2f}")
print(f"Sobregiro: ${corriente._sobregiro:.2f}")

controller.consignar("005", 500)

print(f"Saldo: ${corriente._saldo:.2f}")
print(f"Sobregiro: ${corriente._sobregiro:.2f}")


# ========================================
# FIN
# ========================================

print("\n========================================")
print("       PRUEBAS FINALIZADAS")
print("========================================")