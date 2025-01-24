import asyncio

from fastapi import HTTPException


def validate_number(number: int) -> None:
    if number < 0:
        raise HTTPException(status_code=400, detail="Number must be non-negative.")


async def perform_async_task(number: int) -> int:
    """Simulates an asynchronous task that doubles a number after a delay."""
    validate_number(number)
    await asyncio.sleep(2)  # Simulate a long-running task
    return number * 2
