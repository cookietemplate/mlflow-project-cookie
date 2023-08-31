import nox

DEFAULT_DIRS = ["."]
COVERAGE_THRESHOLD = None


@nox.session(reuse_venv=True, tags=["lint"])
def black(session):
    """Run the code formatter.(black)"""
    files = session.posargs or DEFAULT_DIRS

    session.install("black")
    session.run("black", "--diff", "--check", *files)


@nox.session(reuse_venv=True, tags=["fmt"])
def black_fmt(session):
    """Format the code.(black)"""
    files = session.posargs or DEFAULT_DIRS

    session.install("black")
    session.run("black", *files)


@nox.session(reuse_venv=True, tags=["lint"])
def isort(session):
    """Import sorting checker.(isort)"""
    files = session.posargs or DEFAULT_DIRS

    session.install("isort")
    session.run("isort", "--check-only", *files)


@nox.session(reuse_venv=True, tags=["fmt"])
def isort_fmt(session):
    """Import sorting formatter.(isort)"""
    files = session.posargs or DEFAULT_DIRS

    session.install("isort")
    session.run("isort", *files)


@nox.session(reuse_venv=True, tags=["lint"])
def ruff(session):
    """Run the code formatter.(ruff)"""
    files = session.posargs or DEFAULT_DIRS

    session.install("ruff")
    session.run("ruff", *files)


@nox.session(reuse_venv=True, tags=["fmt"])
def ruff_fmt(session):
    """Format the code.(ruff)"""
    files = session.posargs or DEFAULT_DIRS

    session.install("ruff")
    session.run("ruff", "--fix", *files)


@nox.session(reuse_venv=True, tags=["style"])
def style(session):
    """Run the style checkers."""
    session.run("nox", "-t", "fmt", external=True)
    session.run("nox", "-t", "lint", external=True)


@nox.session(python=False, tags=["prepare"])
def prepare(session):
    """Prepare the project for development."""
    session.run("pre-commit", "install", external=True)
    session.run("pre-commit", "run", "--all-files", "--show-diff-on-failure", external=True)
