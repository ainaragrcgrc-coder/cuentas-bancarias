# Sistema de Cuentas Bancarias

Proyecto de programación orientada a objetos desarrollado en Python para modelar y gestionar diferentes tipos de cuentas bancarias.

El sistema permite trabajar con una cuenta base, una cuenta de ahorros y una cuenta corriente, aplicando conceptos de encapsulación, herencia y polimorfismo.

---

## Objetivo

Diseñar e implementar un sistema de cuentas bancarias utilizando programación orientada a objetos.

El proyecto permite:

- Crear diferentes tipos de cuentas.
- Realizar consignaciones.
- Realizar retiros.
- Calcular intereses mensuales.
- Aplicar comisiones.
- Gestionar cuentas de ahorro activas e inactivas.
- Gestionar sobregiros en cuentas corrientes.
- Mostrar la información de las cuentas.
- Gestionar las operaciones mediante un controller.
- Comprobar el funcionamiento mediante pruebas automáticas.

---

## Tecnologías utilizadas

- Python 3.14.7
- Pytest 9.1.1
- Programación Orientada a Objetos (POO)
- UML
- Mermaid
- Git
- GitHub

---

## Estructura del proyecto

```text
cuentas-bancarias/
│
├── controller/
│   ├── __init__.py
│   └── cuenta_controller.py
│
├── cuenta.py
├── cuenta_ahorros.py
├── cuenta_corriente.py
├── main.py
├── prueba.py
├── test_cuentas.py
├── README.md
│
└── uml/
    └── diagrama-clases.md