from fastapi import FastAPI, Query, File, UploadFile

app = FastAPI()





# User Interface queries
@app.post("/answer_query_from_user_provided_text_file")
async def answer_query_from_user_provided_text_file (query: str = Query(..., title="User Query", max_length=50), file: UploadFile = File(...)):
        if not query:
                return {"answer": "Please provide a query"}
            elif not file or not file.filename.endswith('.txt'):
                return {"answer": "Please upload a .txt file"}
      else:
        file_contents = await file.read()
        try:
           return {"message": "/Bagath"}
        
