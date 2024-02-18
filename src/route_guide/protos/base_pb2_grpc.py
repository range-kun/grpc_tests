# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src.route_guide.protos import base_pb2 as base__pb2


class RouteGuideStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFeature = channel.unary_unary(
                '/RouteGuide/GetFeature',
                request_serializer=base__pb2.Point.SerializeToString,
                response_deserializer=base__pb2.Feature.FromString,
                )
        self.ListFeatures = channel.unary_stream(
                '/RouteGuide/ListFeatures',
                request_serializer=base__pb2.Rectangle.SerializeToString,
                response_deserializer=base__pb2.Feature.FromString,
                )


class RouteGuideServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetFeature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFeatures(self, request, context):
        """A server-to-client streaming RPC.

        Obtains the Features available within the given Rectangle.  Results are
        streamed rather than returned at once (e.g. in a response message with a
        repeated field), as the rectangle may cover a large area and contain a
        huge number of features.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RouteGuideServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFeature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeature,
                    request_deserializer=base__pb2.Point.FromString,
                    response_serializer=base__pb2.Feature.SerializeToString,
            ),
            'ListFeatures': grpc.unary_stream_rpc_method_handler(
                    servicer.ListFeatures,
                    request_deserializer=base__pb2.Rectangle.FromString,
                    response_serializer=base__pb2.Feature.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RouteGuide', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RouteGuide(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetFeature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RouteGuide/GetFeature',
            base__pb2.Point.SerializeToString,
            base__pb2.Feature.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFeatures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/RouteGuide/ListFeatures',
            base__pb2.Rectangle.SerializeToString,
            base__pb2.Feature.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)