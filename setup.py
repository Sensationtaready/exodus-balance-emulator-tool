from setuptools import setup, find_packages

setup(
    name="exodus-balance-emulator-tool",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "exodus-emulator=exodus_balance_emulator_tool.cli:main",
        ],
    },
    author="Your Name",
    description="Exodus Fake Balance Emulator Tool",
    python_requires=">=3.8",
)