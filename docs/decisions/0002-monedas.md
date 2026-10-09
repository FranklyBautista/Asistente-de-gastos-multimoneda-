# 0002 — Modelo de monedas

- **Estado:** aceptada
- **Fecha:** 2026-10-09

## Contexto

El usuario maneja bolívares, pesos colombianos, dólares y USDT a la vez. Las tasas del Bs varían por fuente (BCV, paralelo, P2P) y mezclar la dirección de una tasa produce totales absurdos.

## Decisión

- Códigos internos: `VES`, `COP`, `USD`, `USDT`. El mapeo `VED` → `VES` se hace solo en `rates/ves.py`.
- USD es la moneda pivote; toda tasa se guarda como `usd_per_unit` (USD por 1 unidad), nunca "Bs por USD".
- USDT es una moneda propia, con cuentas y tasa propias; no se trata como USD.
- Cada movimiento se guarda en su moneda original con un snapshot `usd_per_unit` y `amount_usd`.
- La fuente de tasa del Bs es una preferencia por usuario.
- Dinero con `Decimal`, nunca `float`; la salida del LLM se convierte en el borde con `Decimal(str(valor))`.
- Los saldos se calculan desde los movimientos; nunca se guardan.
- Si la moneda es ambigua (confianza < 0.8) se pregunta con botones y no se guarda nada hasta la respuesta.

## Consecuencias

- El historial no cambia cuando se mueve el mercado.
- Los totales se presentan por moneda; el consolidado en USD indica la fuente de tasa usada.
