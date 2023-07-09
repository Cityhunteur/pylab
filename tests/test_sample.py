from __future__ import annotations

from typing import AsyncIterator

import pytest


def inc(x: int) -> int:
    return x + 1


def test_inc():
    assert inc(3) == 4


async def generator() -> AsyncIterator[int]:
    for i in range(3):
        yield i


@pytest.mark.asyncio
async def test_generator() -> None:
    results = [item async for item in generator()]
    assert [0, 1, 2] == results
