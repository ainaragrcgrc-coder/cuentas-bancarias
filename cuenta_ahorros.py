from cuenta import Cuenta


class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasa_anual: float):
        super().__init__(saldo, tasa_anual)

        self.activa = saldo >= 10000

    def consignar(self, cantidad: float):
        if not self.activa:
            raise ValueError("La cuenta de ahorros está inactiva.")

        super().consignar(cantidad)

        self.activa = self._saldo >= 10000

    def retirar(self, cantidad: float):
        if not self.activa:
            raise ValueError("La cuenta de ahorros está inactiva.")

        super().retirar(cantidad)

        self.activa = self._saldo >= 10000

    def extracto_mensual(self):
        if self._numero_retiros > 4:
            retiros_adicionales = self._numero_retiros - 4
            self._comision_mensual += retiros_adicionales * 1000

        super().extracto_mensual()

        self.activa = self._saldo >= 10000

    def imprimir(self):
        total_transacciones = (
            self._numero_consignaciones + self._numero_retiros
        )

        return (
            f"Saldo: ${self._saldo:.2f}\n"
            f"Comisión mensual: ${self._comision_mensual:.2f}\n"
            f"Total de transacciones: {total_transacciones}"
        )