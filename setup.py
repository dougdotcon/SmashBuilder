#!/usr/bin/env python3
"""
🔥 SmashBuilder - Setup de Instalação 🔥
Configuração para instalação do pacote SmashBuilder
"""

from setuptools import setup, find_packages
from pathlib import Path

# Ler o README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Ler requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = requirements_file.read_text(encoding="utf-8").strip().split("\n")
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]

setup(
    name="smashbuilder",
    version="1.0.0",
    author="SmashBuilder Team",
    author_email="dev@smashbuilder.com",
    description="🔥 Calculadora avançada de builds para League of Legends com interface cyberpunk 🔥",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smashbuilder/smashbuilder",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "smashbuilder=cyberpunk_terminal:main",
            "smashbuilder-cli=cli.app:app",
            "smashbuilder-launcher=start_cyberpunk:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["data/*.json", "data/*.yaml", "*.md", "*.txt"],
    },
    keywords=[
        "league of legends",
        "lol",
        "build calculator",
        "gaming",
        "cyberpunk",
        "terminal",
        "cli",
        "stats",
        "dps",
        "calculator"
    ],
    project_urls={
        "Bug Reports": "https://github.com/smashbuilder/smashbuilder/issues",
        "Source": "https://github.com/smashbuilder/smashbuilder",
        "Documentation": "https://smashbuilder.readthedocs.io/",
    },
)
