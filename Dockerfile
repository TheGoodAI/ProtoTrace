FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml ./
COPY src/ ./src/
RUN pip install --no-cache-dir -e .

COPY scripts/ ./scripts/
COPY config/ ./config/
COPY data/ ./data/

ENV KG_DEMO_HOST=0.0.0.0
ENV KG_DEMO_PORT=8000
ENV KG_LOCAL_STATE_DIR=/app/local_state_ui

EXPOSE 8000

CMD ["python", "scripts/run_demo_ui.py"]
