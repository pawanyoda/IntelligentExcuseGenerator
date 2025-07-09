from unittest.mock import patch, MagicMock
from src.models.excuse_generator import ExcuseGenerator
import pytest


@pytest.mark.filterwarnings("ignore:Model load failed")
def test_mock_generator():
    with patch('src.models.excuse_generator.pipeline', side_effect=Exception("Test error")):
        gen = ExcuseGenerator()
        assert gen.using_mock is True
        result = gen.generate("school", "forgot homework")
        assert "[MOCK]" in result
        assert "school excuse" in result

def test_real_generator():
    mock_generator_fn = MagicMock()
    mock_generator_fn.return_value = [{"generated_text": "Real model output"}]

    with patch('src.models.excuse_generator.pipeline', return_value=mock_generator_fn):
        gen = ExcuseGenerator()
        result = gen.generate("work", "deadline")

        assert "Real model output" in result
        assert gen.using_mock is False
        mock_generator_fn.assert_called_once_with("work excuse: deadline", max_length=100)
