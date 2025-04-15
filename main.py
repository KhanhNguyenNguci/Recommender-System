# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Cho phép gọi từ frontend (Next.js localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # có thể đổi sang ['http://localhost:3000']
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model và dữ liệu
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

class BookRequest(BaseModel):
    book_name: str

@app.post("/recommend")
def recommend_book(req: BookRequest):
    book_name = req.book_name
    books_list = []
    poster_url = []

    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    for book_id in suggestion[0]:
        book = book_pivot.index[book_id]
        books_list.append(book)
        idx = np.where(final_rating['title'] == book)[0][0]
        poster_url.append(final_rating.iloc[idx]['image_url'])

    return {
        "recommended_books": books_list,
        "poster_urls": poster_url
    }
