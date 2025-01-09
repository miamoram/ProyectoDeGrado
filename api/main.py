import os
from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
from segmentation import get_image_from_bytes, get_yolo
import uvicorn
import cv2

yolo_obj = get_yolo(model_name="best_yolo11.pt", model_path="api/model/")

app = FastAPI(
    title="API Clasificación de residuos Eco Sistema 🌎♻️",
    description="""A partír de una imágen realiza la identificación y clasificación de residuos, basado en un modelo de identificación de objetos personalizado""",
    version="0.0.1",
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/notify/v1/health')
def get_health():
    """
    Usado en K8S
    readinessProbe:
        httpGet:
            path: /notify/v1/health
            port: 80
    livenessProbe:
        httpGet:
            path: /notify/v1/health
            port: 80
    :return:
        dict(msg='OK')
    """
    return dict(msg='OK')


@app.post("/object-to-json")
async def detect_trash_return_json_result(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = yolo_obj.model(input_image)
    json_result = results[0].summary()
    return json_result
    #detect_res = results.pandas().xyxy[0].to_json(orient="records")  # JSON img1 predictions
    #detect_res = json.loads(detect_res)
    #return {"result": detect_res}


@app.post("/object-to-img")
async def detect_trash_return_base64_img(file: bytes = File(...)):
    input_image = get_image_from_bytes(file)
    results = yolo_obj.model(input_image)    
    # Obtener la imagen anotada
    annotated_image = results[0].plot()  # `plot` genera la imagen con anotaciones    
    # Convertir la imagen anotada a formato JPEG
    _, buffer = cv2.imencode('.jpg', annotated_image)
    return Response(content=buffer.tobytes(), media_type="image/jpeg")

    """results.render()  # updates results.imgs with boxes and labels
    for img in results.ims:
        bytes_io = io.BytesIO()
        img_base64 = Image.fromarray(img)
        img_base64.save(bytes_io, format="jpeg")
    return Response(content=bytes_io.getvalue(), media_type="image/jpeg")"""


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)