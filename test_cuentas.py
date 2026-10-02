import pytest

from cuenta import Cuenta
from cuenta_ahorros import CuentaAhorros
from cuenta_corriente import CuentaCorriente


# =========================================
# PRUEBAS DE CUENTA
# =========================================

def test_consignar_cuenta():
    cuenta = Cuenta(10000, 0.12)

    cuenta.consignar(2000)

    assert cuenta._saldo == 12000
    assert cuenta._numero_consignaciones == 1


def test_retirar_cuenta():
    cuenta = Cuenta(10000, 0.12)

    cuenta.retirar(3000)

    assert cuenta._saldo == 7000
    assert cuenta._numero_retiros == 1


def test_retirar_sin_saldo_suficiente():
    cuenta = Cuenta(10000, 0.12)

    with pytest.raises(ValueError):
        cuenta.retirar(15000)


def test_calcular_interes_mensual():
    cuenta = Cuenta(12000, 0.12)

    cuenta.calcular_interes_mensual()

    assert cuenta._saldo == 12120


# =========================================
# PRUEBAS DE CUENTA DE AHORROS
# =========================================

def test_cuenta_ahorros_activa():
    cuenta = CuentaAhorros(10000, 0.12)

    assert cuenta.activa is True


def test_cuenta_ahorros_inactiva():
    cuenta = CuentaAhorros(9000, 0.12)

    assert cuenta.activa is False


def test_cuenta_ahorros_se_inactiva_al_retirar():
    cuenta = CuentaAhorros(12000, 0.12)

    cuenta.retirar(3000)

    assert cuenta._saldo == 9000
    assert cuenta.activa is False


def test_cuenta_ahorros_no_permite_operaciones_inactiva():
    cuenta = CuentaAhorros(9000, 0.12)

    with pytest.raises(ValueError):
        cuenta.consignar(1000)

    with pytest.raises(ValueError):
        cuenta.retirar(1000)


def test_comision_por_retiros_adicionales():
    cuenta = CuentaAhorros(20000, 0.12)

    cuenta.retirar(100)
    cuenta.retirar(100)
    cuenta.retirar(100)
    cuenta.retirar(100)
    cuenta.retirar(100)

    cuenta.extracto_mensual()

    assert cuenta._comision_mensual == 1000


# =========================================
# PRUEBAS DE CUENTA CORRIENTE
# =========================================

def test_cuenta_corriente_sobregiro():
    cuenta = CuentaCorriente(1000, 0.12)

    cuenta.retirar(1500)

    assert cuenta._saldo == 0
    assert cuenta._sobregiro == 500


def test_cuenta_corriente_reduce_sobregiro():
    cuenta = CuentaCorriente(1000, 0.12)

    cuenta.retirar(1500)
    cuenta.consignar(300)

    assert cuenta._saldo == 0
    assert cuenta._sobregiro == 200


def test_cuenta_corriente_cancela_sobregiro_y_aumenta_saldo():
    cuenta = CuentaCorriente(1000, 0.12)

    cuenta.retirar(1500)
    cuenta.consignar(500)

    assert cuenta._saldo == 0
    assert cuenta._sobregiro == 0


def test_cuenta_corriente_excedente_sobregiro():
    cuenta = CuentaCorriente(1000, 0.12)

    cuenta.retirar(1500)
    cuenta.consignar(800)

    assert cuenta._saldo == 300
    assert cuenta._sobregiro == 0


def test_cuenta_corriente_cuenta_transacciones():
    cuenta = CuentaCorriente(1000, 0.12)

    cuenta.retirar(1500)
    cuenta.consignar(300)
    cuenta.consignar(500)

    total_transacciones = (
        cuenta._numero_consignaciones + cuenta._numero_retiros
    )

    assert total_transacciones == 3