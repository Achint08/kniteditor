"""An editor for knitting projects."""

__version__ = "1.0.2"


def main(*args, **kw):
    """Open the kniteditor window."""
    from .EditorWindow import main
    main()

__all__ = ["main"]
