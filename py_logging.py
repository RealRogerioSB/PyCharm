import logging
import math

logging.basicConfig(
    filename="./docs/logs.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M",
    encoding="utf-8",
    filemode="w"
)

logger = logging.getLogger()

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")


def quadradic_formula(a, b, c):
    logger.info(f"Fórmula Quadrática: {a}, {b}, {c}")
    logger.debug("Computando a fórmula para 2 raízes...")
    
    root1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    root2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    
    logger.debug("Retornando a fórmula")
    
    return f"({root1}, {root2})"


roots = quadradic_formula(1, 0, -4)
print(roots)
