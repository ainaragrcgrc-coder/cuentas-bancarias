from cuenta import Cuenta
from cuenta_ahorros import CuentaAhorros
from cuenta_corriente import CuentaCorriente


class CuentaController:

    def __init__(self):
        self._cuentas = {}

    def crear_cuenta(
        self,
        numero: str,
        tipo: str,
        saldo: float,
        tasa_anual: float
    ):
        if tipo == "base":
            cuenta = Cuenta(saldo, tasa_anual)

        elif tipo == "ahorros":
            cuenta = CuentaAhorros(saldo, tasa_anual)

        elif tipo == "corriente":
            cuenta = CuentaCorriente(saldo, tasa_anual)

        else:
            raise ValueError("Tipo de cuenta no válido.")

        self._cuentas[numero] = cuenta

        return cuenta

    def obtener_cuenta(self, numero: str):
        if numero not in self._cuentas:
            raise ValueError("La cuenta no existe.")

        return self._cuentas[numero]

    def consignar(self, numero: str, cantidad: float):
        cuenta = self.obtener_cuenta(numero)
        cuenta.consignar(cantidad)

    def retirar(self, numero: str, cantidad: float):
        cuenta = self.obtener_cuenta(numero)
        cuenta.retirar(cantidad)

    def realizar_extracto_mensual(self, numero: str):
        cuenta = self.obtener_cuenta(numero)
        cuenta.extracto_mensual()

    def mostrar_cuenta(self, numero: str):
        cuenta = self.obtener_cuenta(numero)
        return cuenta.imprimir()