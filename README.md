# Ecommerce Sistema — Control Roga

Backend (FastAPI + Postgres) para el dashboard Control Roga. Primer modulo: incidencias (persisten aunque se recalculen las ventas).

## Deploy
Desplegado en Railway, conectado a este repo (carpeta `backend/`). Variable `DATABASE_URL` viene del servicio Postgres del mismo proyecto Railway.

## Endpoints
- GET /health
- GET /incidencias
- POST /incidencias
- PATCH /incidencias/{id}
