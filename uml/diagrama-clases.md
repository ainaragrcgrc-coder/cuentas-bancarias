# Diagrama de Clases UML - Sistema de Cuentas Bancarias

El sistema está compuesto por una clase base `Cuenta`, dos clases especializadas y un controlador encargado de gestionar las operaciones sobre las cuentas.

Las clases principales son:

- `Cuenta`
- `CuentaAhorros`
- `CuentaCorriente`
- `CuentaController`

`CuentaAhorros` y `CuentaCorriente` heredan de `Cuenta`.

`CuentaController` gestiona la creación y las operaciones de las diferentes cuentas.

---

## Diagrama de clases

```mermaid
classDiagram

    class Cuenta {
        #float _saldo
        #int _numero_consignaciones
        #int _numero_retiros
        #float _tasa_anual
        #float _comision_mensual

        +__init__(saldo: float, tasa_anual: float)
        +consignar(cantidad: float) None
        +retirar(cantidad: float) None
        +calcular_interes_mensual() None
        +extracto_mensual() None
        +imprimir() str
    }

    class CuentaAhorros {
        +bool activa

        +__init__(saldo: float, tasa_anual: float)
        +consignar(cantidad: float) None
        +retirar(cantidad: float) None
        +extracto_mensual() None
        +imprimir() str
    }

    class CuentaCorriente {
        #float _sobregiro

        +__init__(saldo: float, tasa_anual: float)
        +consignar(cantidad: float) None
        +retirar(cantidad: float) None
        +extracto_mensual() None
        +imprimir() str
    }

    class CuentaController {
        -dict _cuentas

        +__init__() None
        +crear_cuenta(numero: str, tipo: str, saldo: float, tasa_anual: float)
        +obtener_cuenta(numero: str)
        +consignar(numero: str, cantidad: float) None
        +retirar(numero: str, cantidad: float) None
        +realizar_extracto_mensual(numero: str) None
        +mostrar_cuenta(numero: str) str
    }

    Cuenta <|-- CuentaAhorros
    Cuenta <|-- CuentaCorriente

    CuentaController --> Cuenta
    CuentaController --> CuentaAhorros
    CuentaController --> CuentaCorriente