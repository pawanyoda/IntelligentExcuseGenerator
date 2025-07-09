import pytest
from unittest.mock import MagicMock, patch
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

@pytest.fixture
def mock_pipeline():
    mock = MagicMock()
    mock.return_value = [{"generated_text": "Test excuse: Mock output"}]
    with patch('transformers.pipeline', new=mock) as mocked_pipeline:
        yield mocked_pipeline
