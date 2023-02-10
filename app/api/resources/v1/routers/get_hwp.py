import glob
import shutil
import os
import re
import olefile
import zipfile
import aiofiles

from subprocess import Popen, PIPE
from fastapi import APIRouter, UploadFile

from common.utils import success_response, error_response
from config import ROOT_DIR

router = APIRouter(
    prefix='/hwp',
    tags=['hwp']
)


def get_hwp(hwp_path, keyword=None):
    result = []
    try:
        with olefile.OleFileIO(hwp_path) as f:
            encoded_text = f.openstream('PrvText').read()  # PrvText 스트림의 내용 꺼내기
            # encoded_text = f.openstream('BodyText').read()  # BodyText 스트림의 내용 꺼내기
            decoded_text = encoded_text.decode('UTF-16')  # 유니코드를 UTF-16으로 디코딩
        if keyword is None:
            return decoded_text
        else:
            for line in decoded_text.split("\n"):
                if keyword in line:
                    result.append(line)
            return result
    except:
        process = Popen(['hwp5txt', hwp_path], stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        data = stdout.decode('utf-8')
        if len(data) < 100:
            return stderr

        if keyword is None:
            return data
        else:
            for line in data.split("\n"):
                if keyword in line:
                    result.append(line)
            return result


def get_hwpx(hwpx_path):
    hwpx_file = hwpx_path
    os.chdir(os.path.dirname(hwpx_file))
    path = os.path.join(os.getcwd(), "hwpx")

    with zipfile.ZipFile(hwpx_file, 'r') as zf:
        zf.extractall(path=path)
    xml_file = os.path.join(os.getcwd(), "hwpx", "Contents", "section0.xml")

    with open(xml_file, encoding='utf-8') as f:
        text = f.read()
    text = re.sub('<[^<]+>', "", text)
    return text


def delete_tmp_file():
    files = glob.glob(ROOT_DIR + '/tmp/*')
    for file in files:
        if os.path.isdir(file):
            shutil.rmtree(file)
        else:
            os.remove(file)


@router.post('/')
async def hwp(hwp_file: UploadFile):
    hwp_data = await hwp_file.read()
    file_path = ROOT_DIR + '/tmp/' + hwp_file.filename
    async with aiofiles.open(file_path, 'wb') as f:
        await f.write(hwp_data)

    if hwp_file.content_type != 'application/haansofthwp':
        return error_response('한글파일이 아닙니다.')

    file_extension = hwp_file.filename.split('.')[-1]

    if file_extension == 'hwp':
        result = get_hwp(file_path)
        delete_tmp_file()
    elif file_extension == 'hwpx':
        result = get_hwpx(file_path)
        delete_tmp_file()
    else:
        delete_tmp_file()
        return error_response('지원하지 않는 확장자입니다.')
    return success_response(result)
