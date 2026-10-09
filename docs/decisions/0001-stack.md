# 0001 — Stack técnico

- **Estado:** aceptada
- **Fecha:** 2026-10-09

## Contexto

Bot de Telegram para registrar gastos en cuatro monedas con extracción por LLM, más una web en la Fase 9. Un solo desarrollador, planes gratuitos y el código como portfolio.

## Decisión

- Bot en Python 3.12 con uv, aiogram 3 (máquina de estados para aclaraciones) y FastAPI solo para webhook y `/health`.
- Pydantic v2 + pydantic-settings para validar la salida del LLM y la configuración.
- Gemini Flash como LLM principal y Groq como alternativa, detrás de una interfaz `LLMClient` propia.
- Postgres en Supabase con psycopg 3 async y SQL explícito (sin ORM ni supabase-py) para tener transacciones reales.
- Migraciones con la Supabase CLI y pruebas de BD con pgTAP.
- APScheduler 3.x (versión mayor fijada) dentro del proceso del bot.
- Calidad: ruff, pyright, pytest, import-linter (reglas de capas) y gitleaks; CI en GitHub Actions.
- Web: Next.js + Tailwind + Recharts + `@supabase/ssr` en Vercel (Fase 9).

## Alternativas descartadas

python-telegram-bot, SQLAlchemy, supabase-py, WhatsApp y herramientas de monorepo (detalle en `docs/STACK_Y_ARQUITECTURA.md`).

## Consecuencias

- El SQL queda visible y versionado; cada repositorio filtra por `user_id` porque el bot usa credenciales de servicio.
- APScheduler en proceso obliga a una sola instancia del bot.
- Cambiar de proveedor de LLM solo requiere un adaptador nuevo.
