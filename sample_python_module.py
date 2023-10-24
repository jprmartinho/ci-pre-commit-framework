"""Some Sample Python Module."""
import logging


def main():
    """Run main function."""
    logger = logging.getLogger(__name__)

    logger.info("An event occured.")


if __name__ == "__main__":
    main()
