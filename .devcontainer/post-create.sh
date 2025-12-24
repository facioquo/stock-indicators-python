#!/bin/bash
set -e

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install core dependencies
echo "Installing core dependencies..."
pip install -r requirements.txt

# Install test dependencies
echo "Installing test dependencies..."
pip install -r requirements-test.txt

echo "✓ Dev container setup complete!"
