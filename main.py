from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

class FormData(BaseModel):
    grammar: str
    opening: int
    callToAction: int
    personalization: int
    persona: int
    business: int
    features: int
    finalScore: float

@app.post("/submit")
async def submit_form(form_data: FormData):
    # In a real application, you'd store the data in a database
    print(form_data.dict())  # Just print the form data for now

    # Send a JSON response back to confirm the data was received
    return JSONResponse(content={"message": "Form data stored successfully!", "data": form_data.dict()})