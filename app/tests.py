import pytest
import httpx

from app import app


@pytest.mark.asyncio
def test_homepage():
    async with httpx.AsyncClient() as client:
        res = await client.get('/')
    assert res.status_code == 200
