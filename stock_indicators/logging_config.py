import logging


def configure_logging(debug=False):
    """Configure logging for the stock_indicators package."""
    # Get the logger for the package
    logger = logging.getLogger("stock_indicators")

    # Set the logging level based on the debug flag
    log_level = logging.DEBUG if debug else logging.WARNING
    logger.setLevel(log_level)

    # Avoid adding multiple handlers if it's already set up
    if not logger.handlers:
        handler = logging.StreamHandler()  # Print logs to console
        handler.setFormatter(
            logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)

    # An initial message to confirm logging setup
    if debug:
        logger.debug("Debug logging is enabled.")
    else:
        logger.warning("Logging level is set to WARNING (default).")
