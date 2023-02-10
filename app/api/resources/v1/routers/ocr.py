import cv2
import easyocr
import numpy as np

from fastapi import UploadFile, APIRouter

from common.utils import success_response

router = APIRouter(
    prefix='/ocr',
    tags=['ocr']
)


def sharpening(src_img):
    sharpening_a = 5.0

    smoothing_mask = np.array([[1 / 16, 1 / 8, 1 / 16], [1 / 8, 1 / 4, 1 / 8], [1 / 16, 1 / 8, 1 / 16]])
    smoothing_out = cv2.filter2D(src_img, -1, smoothing_mask)
    blr = cv2.GaussianBlur(smoothing_out, (0, 0), 2)
    dst = np.clip((1 + sharpening_a) * smoothing_out - sharpening_a * blr, 0, 255).astype(np.uint8)
    return dst


@router.post("/")
async def ocr_docs(image_file: UploadFile):
    image_data = await image_file.read()
    reader = easyocr.Reader(['ko', 'en'])
    encoded_img = np.fromstring(image_data, dtype=np.uint8)
    img = cv2.imdecode(encoded_img, cv2.IMREAD_GRAYSCALE)

    x1, x2 = 192, 832
    y1, y2 = 52, 67
    sharpening_a = 5.0

    cropped_img = img[y1:y2, x1:x2]
    cropped_img = cv2.resize(cropped_img, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    dst = sharpening(cropped_img)
    dst = sharpening(dst)

    return success_response(
        ' '.join(' '.join(reader.readtext(dst, detail=0)).split()[1:])
        # ' '.join(' '.join(reader.readtext(dst, detail=0)).split())
    )

