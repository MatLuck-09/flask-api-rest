from app.config import APP_PORT
from app import create_app


def main() -> None:
    app = create_app()
    app.run(port=APP_PORT)


if __name__ == "__main__":
    main()
