"""A simple greeting module."""


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("World"))
