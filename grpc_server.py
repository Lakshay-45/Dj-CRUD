from concurrent import futures
import logging
import time
import grpc
from grpc_requests import greeter_pb2
from grpc_requests import greeter_pb2_grpc

# THis class inherits from generator service
class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    # Implementing the Greeter service
    def SayHello(self, request, context):
        logging.info(f"Received request for name: {request.name}")
        response_message = f"Hello, {request.name}!"
        return greeter_pb2.HelloReply(message=response_message)


def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add the servicer to the server
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    # Bind the server to a port
    port = "50051"
    server.add_insecure_port(f"[::]:{port}")

    # Start the server
    server.start()
    logging.info(f"gRPC server started on port {port}. Press CTRL+C to stop.")

    # Keep the server running
    try:
        while True:
            time.sleep(86400)  # Sleep for a day
    except KeyboardInterrupt:
        server.stop(0)
        logging.info("gRPC server stopped.")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()