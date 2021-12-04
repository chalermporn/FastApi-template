# from fastapi import FastAPI
# from pydantic import BaseModel
# from routers import file,book
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn 
# app = FastAPI()



# app.include_router(book.router)
# app.include_router(file.router)
 


from app.handlers import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host = '127.0.0.1', port = 8080, reload = True, debug = True)