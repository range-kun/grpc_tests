import io

import grpc
from openpyxl import load_workbook

from src.send_file.grpc_files.file_pb2 import FileRequest, FileResponse
from src.send_file.grpc_files.file_pb2_grpc import DownloadStub


def get_file(file_name: str, stub: DownloadStub):
    file_data = stub.DownloadFile(FileRequest(filename=file_name))

    bytes_data = bytearray()
    for grpc_data in file_data:
        if grpc_data.file_size:
            print(f"File size {grpc_data.file_size}")
            continue
        bytes_data.extend(grpc_data.chunk)

    wb = load_workbook(filename=io.BytesIO(bytes_data), data_only=True)
    sh = wb["Лист1"]
    print(sh["A2"].value)

    # path = f"files/{file_name}"
    # with open(path, "wb") as file:
    #     file.write(bytes_data)


def run():
    with grpc.insecure_channel("[::]:50051") as channel:
        stub = DownloadStub(channel)
        print("__Get xsls File__")
        get_file("file_3.xlsx", stub)
        # print("___Get Not existed file__")
        # get_file("random_shit.py", stub)

        # get_file("file_1.pdf", stub)
        # print("___Get YAML File___")
        # get_file("file_2.yaml", stub)


if __name__ == '__main__':
    run()
