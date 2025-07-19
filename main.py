import crud
import random
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Let's find the answer",
    description="A fun fortune-telling API that gives you random answers like a Magic 8 Ball."
)

class Answer(BaseModel):
    text: str

answer_list = ["YES", "NO", "MAYBE"]


@app.get("/8ball")
def get_answer():
    ## TODO: Random answer
    return { "answer": "Okay inw za"}


@app.post("/8ball")
def add_answer(new_answer: Answer):
    ## TODO: Update list of answer with new_answer
    return answer_list


# TODO Get all answer
@app.get("/8ball/all")
def get_all_answer():
    raise HTTPException(status_code=404, detail="No answers available")


# TODO Update answer
@app.put("/8ball/{id}")
def update_answer(id: int, answer: Answer):
    ...


# TODO Delete answer
@app.delete("/8ball/{id}")
def delete_answer(id: int):
    ...