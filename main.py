from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()
origins = [
    "https://samantha-who.github.io",  # Replace this with your exact domain
    "http://localhost",  # Allow requests from localhost for testing
    "http://127.0.0.1",  # Allow requests from localhost (IP address)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow requests from these domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# In-memory storage for form data
form_data_storage = []

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
