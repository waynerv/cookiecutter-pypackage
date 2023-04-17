from pathlib import Path

import pytest


@pytest.fixture(scope='session')
def output_folder() -> Path:
    folder = Path(__file__).parent.parent / 'output'
    return folder


@pytest.fixture(scope='session')
def fixtures_folder() -> Path:
    folder = Path(__file__).parent / 'fixtures'
    return folder
