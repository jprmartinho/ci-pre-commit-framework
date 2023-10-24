"""Some Sample Python Module."""
import logging


def main():
    """Run main function."""
    logger = logging.getLogger(__name__)
    print("Event processing.")
    logger.info("An event was processed.")


if __name__ == "__main__":
    main()
