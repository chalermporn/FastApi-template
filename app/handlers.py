from fastapi import FastAPI, Depends, Header, HTTPException, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import fund, items
from .routers import book, file
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import logging


app = FastAPI(title="FastAPI Test Fund",
              description="Description and technical detail of APIs, Live on Medium | Author : Promlert Pearrukkrai",
              version="0.0.1")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/api/v1/info")
async def information():
    return {"app_name": app.title, "version": app.version, "documents_path": "/docs"}


@app.on_event("startup")
async def startup_event():
    logging.info("Application start")


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Application shutdown")
origins = [
    "http://localhost:5000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# async def get_x_card_id_token(x_card_id: str = Header(...)):
#     try:
#         if not TSUTAYA_MEMBER.get(x_card_id, False):
#             raise HTTPException(status_code = 400, detail = "X-Card-ID header invalid")
#     except Exception as e:
#         logging.error(e)
#         raise HTTPException(status_code = 400, detail = "X-Card-ID header invalid")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health_check")
async def root():
    return {"date_current": datetime.now().strftime("%Y-%m-%d")
            }  # .strftime("%m/%d/%Y, %H:%M:%S")}
app.include_router(
    book.router,
    prefix="/book/v1",
    tags=["book"],
    responses={404: {"message": "Not found"}},
)

app.include_router(
    file.router,
    prefix="/file/v1",
    tags=["file"],
    responses={404: {"message": "Not found"}},
)

app.include_router(
    fund.router,
    prefix="/api/fund",
    tags=["fund"],
    responses={404: {"message": "Not found"}},
)

app.include_router(
    items.router,
    prefix="/view/item",
    tags=["item"],
    responses={404: {"message": "Not found"}},
)
