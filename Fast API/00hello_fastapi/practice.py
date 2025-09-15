from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

fast_api_app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length = 2, max_length = 40)
    author: str = Field(min_length = 2, max_length = 40)
    description: str = Field(min_length= 2, max_length= 200)
    rating: int 

BOOKS = []

@fast_api_app.get("/")
def read_all_books():
    return BOOKS

@fast_api_app.post("/")
def create_book(book: Book):
    BOOKS.append(book)
    return book

@fast_api_app.put("/{book_id}")
def update_book(book_id: UUID, updated_book: Book):
    counter = 0
    for book in BOOKS:
        counter +=1
        if book.id == book_id:
            BOOKS[counter - 1] = updated_book
            return updated_book
        
        raise HTTPException(
            status_code=404,
            detail=f"Book with id {book_id} not found",
        )


@fast_api_app.delete("/{book_id}")
def delete_book(book_id: UUID):
    counter = 0
    for book in BOOKS:
        counter += 1
        if book.id == book_id:
            BOOKS.pop(counter - 1)
            return f"Book with id {book_id} has been deleted"
        raise HTTPException(
            status_code=404,
            detail=f"Book with id {book_id} not found",
        )