from concurrent import futures
import os

import grpc

from src.send_file.grpc_files import file_pb2_grpc
from src.send_file.grpc_files import file_pb2


def upload_file(file_name):
    path = f"files/{file_name.filename}"

    st = os.stat(path).st_size
    yield file_pb2.FileResponse(file_size=st)
    with open(path, "rb") as file:
        while True:
            chunk = file.read(1024)
            if chunk:
                yield file_pb2.FileResponse(chunk=chunk)
            else:
                return


class DownloadServer:
    def DownloadFile(self, request, context):
        try:
            return upload_file(request)
        except FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(f"File with file name {request.filename} not found")
            raise grpc.RpcError()


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_pb2_grpc.add_DownloadServicer_to_server(
        DownloadServer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("server started")
    server.wait_for_termination()
