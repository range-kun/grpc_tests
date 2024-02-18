import grpc

from src.route_guide.protos.base_pb2 import Point, Rectangle
from src.route_guide.protos.base_pb2_grpc import RouteGuideStub


def guide_get_feature(stub: RouteGuideStub):
    feature = stub.GetFeature(Point(latitude=409146138, longitude=-746188906))
    if not feature.location:
        print("Server returned incomplete feature")
        return

    if feature.name:
        print(f"Feature called {feature.name} at {feature.location}")
    else:
        print(f"Found no feature at {feature.location}")


def guide_list_feature(stub: RouteGuideStub):
    rectangle = Rectangle(
        lo=Point(latitude=400000000, longitude=-750000000),
        hi=Point(latitude=420000000, longitude=-730000000),
        )
    print("Looking for features between 40, -75 and 42, -73")
    features = stub.ListFeatures(rectangle)
    print(features)

    for feature in features:
        print(f"Feature called {feature.name} at {feature.location}")


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = RouteGuideStub(channel)
        print("___Get FEATURE___")
        guide_get_feature(stub)
        print("____ListFeature____")
        guide_list_feature(stub)


if __name__ == '__main__':
    run()
