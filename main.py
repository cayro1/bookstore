import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)