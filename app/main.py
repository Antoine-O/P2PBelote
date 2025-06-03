from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse, Response


app = FastAPI()

@app.head("/ping")
async def ping():
    return Response(status_code=status.HTTP_200_OK)

