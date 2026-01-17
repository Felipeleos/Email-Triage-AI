from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.classifier import classify_email

app = FastAPI(title="AutoU Email Triage AI")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/classify", response_class=HTMLResponse)
def classify(request: Request, email_text: str = Form(...)):
    result = classify_email(email_text)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result, "email_text": email_text}
    )
