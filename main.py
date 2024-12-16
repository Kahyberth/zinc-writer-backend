from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from controller.zinc import Zinc

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        
        contents = file.file.read().decode("utf-8")
        print("Contenido del archivo recibido:")
        print(contents)

        zinc_instance = Zinc(n=5, m=5)
        result = zinc_instance.read_data(contents.splitlines())

        return result
    except ValueError as ve:
        print("Error de valor:", str(ve))
        raise HTTPException(status_code=400, detail=f"Error de valor: {str(ve)}")
    except Exception as e:
        print("Error inesperado:", str(e))
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")
