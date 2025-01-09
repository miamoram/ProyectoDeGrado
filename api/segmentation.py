import torch
from PIL import Image
import io
import os

from yolo import YOLOv11Model

def get_yolov5(model_path=None):
    # Obtener el directorio raíz del proyecto
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if model_path is None:
        # Ruta por defecto al modelo local
        model_path = os.path.join(root_dir, 'api/model/best_40_epoch.pt')
    else:
        # Convertir la ruta del modelo a una ruta absoluta basada en el directorio raíz
        model_path = os.path.join(root_dir, model_path)
    
    # Cargar el modelo desde la ruta especificada
    model = torch.hub.load(os.path.join(root_dir, 'api/yolov5'), 'custom', path=model_path, source='local', force_reload=True)
    #TODO debe obtenerse por parámetro
    model.conf = float(os.environ.get("CONFIDENCE", 0.5))
    return model

def get_image_from_bytes(binary_image, max_size=1024):
    input_image = Image.open(io.BytesIO(binary_image)).convert("RGB")
    width, height = input_image.size
    resize_factor = min(max_size / width, max_size / height)
    resized_image = input_image.resize(
        (
            int(input_image.width * resize_factor),
            int(input_image.height * resize_factor),
        )
    )
    return resized_image

def get_yolo(model_path=None, model_name="best_model.pt"):
    # Ruta al modelo YOLOv11 entrenado localmente
    #model_path = "path/to/your/yolov11_model.pt"
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(root_dir, model_path, model_name)
    
    # Crear una instancia de la clase
    yolo = YOLOv11Model(model_path=model_path, confidence=0.5, overlap=0.4)
    
    # Cargar el modelo
    yolo.load_model()
    
    # Realizar predicción en una imagen
    #image_path = "/home/miguel/Downloads/1000354364.jpg"
    #predictions = yolo.predict(image_path)
    
    # Imprimir las predicciones
    #for pred in predictions:
    #    print(pred)
    return yolo
    # Visualizar las predicciones
    #yolo.visualize_predictions(image_path, predictions, output_path="output_image.jpg")