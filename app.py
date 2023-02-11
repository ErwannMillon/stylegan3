import random

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from gen_images import api_generate_images

app = FastAPI()

base_model = "dock_model/alien.pkl"

@app.post("/get_img")
def get_img(n: int = 1):
    seeds = random.choices(range(100000), k=n)
    img_path = api_generate_images(
        base_model,
        [1, 2],
        1,
        "const",
        "./tmp",
        (0., 0.),
        0,
    )
    return FileResponse(img_path)
    
if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)