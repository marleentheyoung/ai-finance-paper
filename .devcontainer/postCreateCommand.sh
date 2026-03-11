#!/usr/bin/env bash
set -euo pipefail

echo "--- running just install ---"
just install

echo "--- verifying just ---"
just --version

echo "--- verifying uv ---"
uv --version

echo "--- verifying claude ---"
claude --version

echo "--- container ready ---"
