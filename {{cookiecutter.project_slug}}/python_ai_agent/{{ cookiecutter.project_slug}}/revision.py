import sys
from alembic import command
from alembic.config import Config

def create_revision(message: str = "revision", autogenerate: bool = True):
    """Create a new database migration revision using Alembic."""
    if len(sys.argv) > 1:
        message = sys.argv[1]

    alembic_cfg = Config("alembic.ini")
    command.revision(alembic_cfg, message=message, autogenerate=True)


if __name__ == "__main__":
    create_revision()
