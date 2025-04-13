import logging

logger = logging.getLogger("{{ cookiecutter.project_slug }}")
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

__all__ = ["logger"]
