# ── Base image ────────────────────────────────────────────────────────────────
# Official Microsoft Python devcontainer base (Debian Bookworm, Python 3.11).
# Provides a non-root `vscode` user and common dev tooling out of the box.
FROM mcr.microsoft.com/devcontainers/python:3.11-bookworm

# ── System packages ───────────────────────────────────────────────────────────
# Install TeX Live (full), latexmk, make, curl, and git.
# texlive-full covers all packages needed for academic papers.
RUN apt-get update && apt-get install -y --no-install-recommends \
    texlive-full \
    latexmk \
    make \
    curl \
    git \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# ── just command runner ───────────────────────────────────────────────────────
# Install the `just` binary directly from the upstream installer script.
# Pinned to a stable channel; the binary lands in /usr/local/bin.
RUN curl --proto '=https' --tlsv1.2 -sSf \
    https://just.systems/install.sh \
    | bash -s -- --to /usr/local/bin

# ── uv Python package manager ─────────────────────────────────────────────────
# uv is a fast drop-in replacement for pip/venv.
# Installed globally so every user shell can invoke it.
RUN curl -Lsf https://astral.sh/uv/install.sh | sh \
    && cp /root/.local/bin/uv /usr/local/bin/uv \
    && cp /root/.local/bin/uvx /usr/local/bin/uvx

# ── Python scientific stack ───────────────────────────────────────────────────
# Install packages as root into the system Python so they are available
# immediately without activating a virtualenv.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        numpy \
        pandas \
        sympy \
        scipy \
        matplotlib \
        statsmodels

# ── Workspace ─────────────────────────────────────────────────────────────────
# The workspace will be mounted at /workspaces/<repo-name> by VS Code.
# No extra steps needed here — devcontainer.json handles the mount.
