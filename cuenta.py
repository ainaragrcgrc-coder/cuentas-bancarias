class Cuenta:
    def __init__(self, saldo: float, tasa_anual: float):
        self._saldo = saldo
        self._numero_consignaciones = 0
        self._numero_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = 0.0

    def consignar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a consignar debe ser mayor que 0.")

        self._saldo += cantidad
        self._numero_consignaciones += 1

    def retirar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")

        if cantidad > self._saldo:
            raise ValueError("No hay saldo suficiente para realizar el retiro.")

        self._saldo -= cantidad
        self._numero_retiros += 1

    def calcular_interes_mensual(self):
        interes = (self._tasa_anual / 12) * self._saldo
        self._saldo += interes

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes_mensual()

    def imprimir(self):
        return (
            f"Saldo: ${self._saldo:.2f}\n"
            f"Consignaciones: {self._numero_consignaciones}\n"
            f"Retiros: {self._numero_retiros}\n"
            f"Tasa anual: {self._tasa_anual * 100:.0f}%\n"
            f"Comisión mensual: ${self._comision_mensual:.2f}"
        )