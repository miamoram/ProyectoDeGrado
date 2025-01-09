import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO
from typing import List

class YOLOv11Model:
    def __init__(self, model_path: str, confidence: float = 0.4, overlap: float = 0.5):
        """
        Inicializa la clase con la ruta al modelo local y parámetros de inferencia.

        Args:
            model_path (str): Ruta al archivo del modelo (.pt).
            confidence (float): Umbral de confianza para las detecciones.
            overlap (float): Umbral de superposición para la supresión no máxima.
        """
        self.model_path = model_path
        self.confidence = confidence
        self.overlap = overlap
        self.model = None

    def load_model(self):
        """
        Carga el modelo YOLO desde un archivo local.
        """
        try:
            self.model = YOLO(self.model_path)
            print(f"Modelo cargado correctamente desde {self.model_path}")
        except Exception as e:
            raise RuntimeError(f"Error al cargar el modelo: {e}")

    def predict(self, image_input):
        """
        Realiza predicciones en una imagen dada.

        Args:
            image_input (str or numpy.ndarray): Ruta de la imagen para realizar inferencia o la imagen en sí.

        Returns:
            dict: Resultados de la predicción, incluyendo las coordenadas de las cajas y etiquetas.
        """
        if self.model is None:
            raise RuntimeError("El modelo no se ha cargado. Por favor, carga el modelo antes de predecir.")
        
        # Verificar si image_input es una ruta, bytes o un objeto de imagen
        if isinstance(image_input, str):
            # Leer la imagen desde la ruta
            image = cv2.imread(image_input)
            if image is None:
                raise FileNotFoundError(f"No se pudo cargar la imagen desde {image_input}")
        elif isinstance(image_input, bytes):
            # Convertir la imagen en bytes a un arreglo numpy
            image = self.get_image_from_bytes(image_input)
        elif isinstance(image_input, Image.Image):
            # Convertir el objeto de imagen a un arreglo numpy
            image = np.array(image_input)
        else:
            raise ValueError("image_input debe ser una ruta de imagen (str), una imagen en bytes (bytes) o un objeto de imagen (PIL.Image.Image)")
        
        # Realizar la inferencia
        results = self.model(image)
        
        # Procesar los resultados según sea necesario
        # Aquí puedes agregar el procesamiento de los resultados
        
        return results

    def visualize_predictions(self, image_path: str, predictions: List[dict], output_path: str = None):
        """
        Visualiza las predicciones en la imagen original.

        Args:
            image_path (str): Ruta de la imagen original.
            predictions (List[dict]): Resultados de las predicciones.
            output_path (str): Ruta para guardar la imagen con anotaciones (opcional).
        """
        # Leer la imagen
        image = cv2.imread(image_path)
        
        # Dibujar las cajas y etiquetas
        for pred in predictions:
            x1, y1, x2, y2 = map(int, pred["box"])
            conf = pred["confidence"]
            cls = pred["class"]
            
            # Dibujar la caja
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"{cls} {conf:.2f}"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # Mostrar o guardar la imagen
        if output_path:
            cv2.imwrite(output_path, image)
            print(f"Imagen con anotaciones guardada en {output_path}")
        else:
            cv2.imshow("Predictions", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
