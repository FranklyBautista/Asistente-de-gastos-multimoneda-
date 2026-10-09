.PHONY: setup check test db-up db-reset

setup:
	cd bot && uv sync

db-up:
	supabase start

db-reset:
	supabase db reset

test:
	cd bot && uv run pytest tests/unit -q

check:
	cd bot && uv run ruff check . && uv run ruff format --check . && uv run pyright && uv run lint-imports && uv run pytest tests/unit -q
	supabase test db
