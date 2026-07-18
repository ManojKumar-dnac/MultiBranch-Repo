"""Greeting business logic."""


def create_greeting(name: str) -> str:
    """Return a greeting for a non-empty, trimmed name."""
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned_name}!"

