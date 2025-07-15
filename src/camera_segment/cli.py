from importlib.metadata import version

__version__ = version("camera-segment")


def main(sysv=None):
    print(f"camera-segment: v{__version__}")


if __name__ == "__main__":  # pragma: no cover
    main()
