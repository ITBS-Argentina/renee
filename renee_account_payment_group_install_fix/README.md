# Renee Account Payment Group Install Fix

Este módulo soluciona un problema de instalación del módulo `account_payment_group` de ADHOC SA. El problema ocurre cuando hay datos legacy en la base de datos que contienen grupos de pagos con líneas a pagar de múltiples cuentas diferentes, lo que causa un error de validación durante la ejecución del hook de post-instalación.

## Problema

El módulo `account_payment_group` incluye un método `_compute_destination_account_id` en el modelo `account.payment` que valida que todas las líneas a pagar pertenezcan a la misma cuenta. Si encuentra múltiples cuentas, lanza una `ValidationError`:

```python
if len(to_pay_account) > 1:
    raise ValidationError(_('To Pay Lines must be of the same account!'))
```

Durante la instalación, el hook `post_init_hook` crea grupos de pagos para pagos existentes, y si hay datos legacy con múltiples cuentas, la instalación falla.

## Solución

Este módulo overridea el método `_compute_destination_account_id` para permitir múltiples cuentas, registrando una advertencia en el log en lugar de lanzar un error, y usando la primera cuenta encontrada.

### Código del override

```python
if len(to_pay_account) > 1:
    _logger.warning('Payment %s has multiple accounts. Using first.', rec.id)
    rec.destination_account_id = to_pay_account[0]
```

## Instrucciones de instalación

### Paso 1: Modificar el código del módulo account_payment_group

**ANTES de instalar el módulo `account_payment_group`, debe modificar manualmente el archivo:**

`odoo/custom/src/account-payment/account_payment_group/models/account_payment.py`

En las líneas 192-194, cambie el código de:

```python
if len(to_pay_account) > 1:
    raise ValidationError(_('To Pay Lines must be of the same account!'))
```

Por:

```python
if len(to_pay_account) > 1:
    _logger.warning('Payment %s has multiple accounts. Using first.', rec.id)
    rec.destination_account_id = to_pay_account[0]
```

**Nota importante:** Esta modificación debe hacerse ANTES de instalar `account_payment_group`. Si ya intentó instalarlo y falló, necesitará limpiar el registro del módulo en la base de datos (ver acciones del servidor incluidas).

### Paso 2: Instalar este módulo

1. Coloque este módulo en `odoo/custom/src/renee/renee_account_payment_group_install_fix/`
2. Reinicie Odoo
3. Instale el módulo `renee_account_payment_group_install_fix`
4. Instale el módulo `account_payment_group`

### Paso 3: Limpiar registro del módulo (si es necesario)

Si previamente intentó instalar `account_payment_group` y falló, use la acción del servidor "Clean account_payment_group" disponible en el menú Administración para limpiar el registro del módulo en la base de datos antes de intentar instalarlo nuevamente.

## Funcionalidades incluidas

- **Override del método de validación**: Permite instalar `account_payment_group` sin errores de validación
- **Acción del servidor para limpieza**: Permite resetear el estado del módulo `account_payment_group` en caso de instalación fallida previa

## Dependencias

- `account_payment_group` (se instala después de este módulo)

## Notas

- Este módulo es temporal y se usa solo para facilitar la instalación de `account_payment_group`
- Una vez instalado `account_payment_group`, puede desinstalar este módulo si no es necesario mantener el override
- Las advertencias sobre múltiples cuentas se registran en los logs de Odoo para seguimiento</content>
<parameter name="filePath">/home/facundo/calyx-servicios/renee/odoo/custom/src/renee/renee_account_payment_group_install_fix/README.md
