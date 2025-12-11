FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /report_generator

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/report_generator \
    RUNNING_IN_CONTAINER=True \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never

COPY pyproject.toml uv.lock ./

RUN uv venv
ENV PATH="/report_generator/.venv/bin:${PATH}"
RUN uv sync --locked

COPY . /report_generator/

CMD ["sleep", "infinity"]