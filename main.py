from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import FineData

# In-memory data storage (resets on server restart)
fine_table = {
    "Krishna": [0, 0, 0],
    "Arjun": [0, 0, 0]
}

app = FastAPI()

# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Get current fine table
@app.get("/data")
def get_data():
    return fine_table

# Update fine table with new data
@app.post("/data")
def update_data(entry: FineData):
    global fine_table
    fine_table = entry.data
    return {"message": "Fine table updated successfully"}

# Add a new name (column)
@app.put("/name")
def add_name(name: str):
    if name not in fine_table:
        # Add a new column with same number of rows as existing
        row_count = len(next(iter(fine_table.values()), []))
        fine_table[name] = [0] * row_count
    return fine_table

# Remove a name (column)
@app.delete("/name/{name}")
def delete_name(name: str):
    if name in fine_table:
        del fine_table[name]
    return fine_table

# Reset all values to 0
@app.delete("/reset")
def reset_data():
    global fine_table
    fine_table = {name: [0] * len(values) for name, values in fine_table.items()}
    return {"message": "All values reset to 0"}
