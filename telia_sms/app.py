from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


app = FastAPI()


class SmsModel(BaseModel):
    phone_number: str
    message: str


class CredentialsModel(BaseModel):
    secret: str
    email: str
    phone_number: str
    password: str


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
        <html>
            <head>
                <title>Telia SMS Python API</title>
            </head>
            <body>
                <h1>Telia SMS Python API</h1>
                <p>Here comes more info.</p>
            </body>
        </html>
    """


@app.get("/contacts")
def contacts():
    return {'message': 'dummy'}


@app.get("/groups")
def groups():
    return {'message': 'dummy'}


@app.post("/sms")
def send_sms():
    return {'message': 'dummy'}


@app.get("/sms")
def read_sms():
    return {'message': 'dummy'}
