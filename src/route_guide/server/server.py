import json
from concurrent import futures

import grpc

from src.converter import protobuf_to_dict
from src.route_guide.protos import base_pb2
from src.route_guide.protos import base_pb2_grpc


def read_route_guide_database():
    feature_list = []
    with open("db.json") as route_guide_db_file:
        for item in json.load(route_guide_db_file):
            feature = base_pb2.Feature(
                name=item["name"],
                location=base_pb2.Point(
                    latitude=item["location"]["latitude"],
                    longitude=item["location"]["longitude"]
                ),
            )
            feature_list.append(feature)
    return feature_list


def get_feature(feature_db, point):
    for feature in feature_db:
        if feature.location == point:
            return feature
    return None


class RouteGuideServicer:
    def __init__(self):
        self.db = read_route_guide_database()

    def GetFeature(self, request, context):
        print("XXXXXXXXXXXXXXXXxx")
        feature = get_feature(self.db, request)
        if feature is None:
            return base_pb2.Feature(name="", location=request)
        return feature

    def ListFeatures(self, request, context):
        dicti = protobuf_to_dict(request)
        left = min(request.lo.longitude, request.hi.longitude)
        right = max(request.lo.longitude, request.hi.longitude)
        top = max(request.lo.latitude, request.hi.latitude)
        bottom = min(request.lo.latitude, request.hi.latitude)
        for feature in self.db:
            if (
                    left <= feature.location.longitude <= right
                    and bottom <= feature.location.latitude <= top
            ):
                yield feature


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    base_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("server started")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
