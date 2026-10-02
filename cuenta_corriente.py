from cuenta import Cuenta


class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)

        self._sobregiro = 0.0

    def retirar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que 0.")

        self._numero_retiros += 1

        if cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            diferencia = cantidad - self._saldo
            self._saldo = 0
            self._sobregiro += diferencia

    def consignar(self, cantidad: float):
        if cantidad <= 0:
            raise ValueError("La cantidad a consignar debe ser mayor que 0.")

        if self._sobregiro > 0:
            if cantidad <= self._sobregiro:
                self._sobregiro -= cantidad
                self._numero_consignaciones += 1
            else:
                excedente = cantidad - self._sobregiro
                self._sobregiro = 0

                super().consignar(excedente)
        else:
            super().consignar(cantidad)

    def extracto_mensual(self):
        super().extracto_mensual()

    def imprimir(self):
        total_transacciones = (
            self._numero_consignaciones + self._numero_retiros
        )

        return (
            f"Saldo: ${self._saldo:.2f}\n"
            f"Comisión mensual: ${self._comision_mensual:.2f}\n"
            f"Total de transacciones: {total_transacciones}\n"
            f"Sobregiro: ${self._sobregiro:.2f}"
        )