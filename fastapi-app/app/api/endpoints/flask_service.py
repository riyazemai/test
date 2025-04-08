from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello from FastAPI"}

@router.get("/call-flask")
async def call_flask():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://127.0.0.1:8111/")
            return {"flask_response": response.text}
    except httpx.RequestError as exc:
        raise HTTPException(status_code=503, detail=f"Error communicating with Flask service: {str(exc)}")