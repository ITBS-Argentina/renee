# Renee Payment Group Fix

Este módulo corrige problemas relacionados con la instalación y funcionamiento del módulo `account_payment_group` de ADHOC SA en sistemas con datos legacy.

## Problemas que Soluciona

### 1. Error de Validación durante Instalación
El módulo `account_payment_group` incluye validaciones estrictas que pueden fallar durante la instalación cuando hay datos existentes con características específicas. Este módulo overridea dichas validaciones para permitir una instalación exitosa.

### 2. Nombres de Grupos de Pago Vacíos
Después de la instalación, los grupos de pago pueden mostrar nombres vacíos ("False") en lugar de nombres descriptivos. Este módulo proporciona una solución automática para asignar nombres basados en los pagos asociados.

### 3. Limpieza de Registro de Módulo
Incluye herramientas para resetear el estado de instalación del módulo `account_payment_group` en caso de fallos previos.

## Funcionalidades

### Override de Validación en Pagos
- **Archivo**: `models/account_payment.py` (no mostrado en estructura actual, pero funcional)
- **Método**: `_compute_destination_account_id`
- **Cambio**: Convierte `ValidationError` en `warning` cuando hay múltiples cuentas, usando la primera cuenta encontrada

### Override de Nombres en Grupos de Pago
- **Archivo**: `models/account_payment_group.py`
- **Método**: `name_get()`
- **Funcionalidad**: Retorna el nombre del primer pago cuando el grupo no tiene nombre propio

### Acción de Servidor para Limpieza
- **Archivo**: `data/ir_actions_server.xml`
- **Funcionalidad**: Elimina dependencias y resetea el estado del módulo `account_payment_group` en la base de datos
- **Acceso**: Disponible en menú Administración > "Clean account_payment_group"

## Instalación y Uso

### Requisitos Previos
- Módulo `account_payment_group` debe estar disponible para instalación
- Si hay fallos previos de instalación, usar la acción de limpieza primero

### Pasos de Instalación
1. Colocar el módulo en `odoo/custom/src/renee/renee_payment_group_fix/`
2. Reiniciar Odoo
3. Instalar el módulo `renee_payment_group_fix`
4. Instalar el módulo `account_payment_group` (este módulo facilita su instalación)
5. Usar la acción "Clean account_payment_group" si es necesario para instalaciones fallidas previas

### Verificación
- Los grupos de pago deberían mostrar nombres descriptivos en lugar de "False"
- Las validaciones de múltiples cuentas generan warnings en logs en lugar de errores
- La instalación de `account_payment_group` debería completarse exitosamente

## Dependencias

- `account_payment_group` (debe instalarse después de este módulo)
- `base`

## Notas Técnicas

- **Override de Modelo**: Este módulo hereda y modifica comportamientos de `account.payment` y `account.payment.group`
- **Acciones de Servidor**: Usa SQL directo para manipulación de base de datos cuando los métodos ORM no son suficientes
- **Logging**: Los casos de múltiples cuentas se registran como warnings para seguimiento
- **Temporal**: Este módulo puede desinstalarse una vez completada la migración exitosa

## Solución de Problemas

### Instalación Fallida de account_payment_group
1. Ejecutar la acción "Clean account_payment_group" desde el menú Administración
2. Verificar logs de Odoo para mensajes de warning sobre múltiples cuentas
3. Reintentar la instalación

### Nombres de Grupos Aún Vacíos
- Verificar que los pagos individuales tengan nombres asignados
- Revisar logs para casos donde no se pudo asignar nombre automáticamente

Este módulo asegura una transición suave al uso de `account_payment_group` en entornos con datos legacy complejos.
