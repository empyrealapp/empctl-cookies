from alembic import command
from alembic.config import Config

def run_migrations(target: str = "head"):
    """Run database migrations using Alembic."""
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    run_migrations()
