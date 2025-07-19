import crud
import random
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

#run "fastapi dev main.py" in root terminal to executeing main.py
app = FastAPI(
    title="Let's find the answer",
    description="A fun fortune-telling API that gives you random answers like a Magic 8 Ball."
)

class Answer(BaseModel):
    text: str

answer_list = ["YES", "NO", "MAYBE"]

#Random answer
from crud import get_random_answer
@app.get("/8ball")
def get_answer():
    ## TODO: Random answer
    answer = get_random_answer()
    return { "answer": answer}

#Post answer
@app.post("/8ball")
def add_answer(new_answer: Answer):
    crud.add_answer(new_answer.text)
    return {'massage':'successfully created'}


# TODO Get all answer
@app.get("/8ball/all")
def get_all_answer():
    answers = crud.get_all_answers()
    #raise HTTPException(status_code=404, detail="No answers available")
    return answers

from crud import update_answer
# TODO Update answer
@app.put("/8ball/{id}")
def update_answer(id: int, answer: Answer):
    is_update = crud.update_answer(id,answer) 
    if is_update == True:
        return {'massage':'updated'}
    else:
        return {'massage':'Error id not found'}


# TODO Delete answer
@app.delete("/8ball/{id}")
def delete_answer(id: int):
    is_deleted = crud.delete_answer(id)
    if is_deleted:
        return {'massage':'answer deleted'}
    else:
        return {'massage': 'Error ID notexits'}