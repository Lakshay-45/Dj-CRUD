import grpc
from django.core.management.base import BaseCommand
from django.conf import settings

# Importing the grpc files
import sys
import os

sys.path.append(os.path.join(settings.BASE_DIR, "grpc_requests"))

import echo_pb2
import echo_pb2_grpc

class Command(BaseCommand):
    help = "Makes a sample grpc request to a public service."

    def handle(self, *args, **options):
        self.stdout.write("Attempting to make a grpc request...")

        # Address of the public grpc server
        server_address = "grpc.postman-echo.com:443"

        try:
            # Creating a connection to the server
            with grpc.insecure_channel(server_address) as channel:

                # Creating a client stub
                stub = echo_pb2_grpc.EchoStub(channel)

                # Create the request message
                request_message = echo_pb2.Request(text="Hello, gRPC")

                self.stdout.write(f"Sending request to {server_address} with message 'Hello, gRPC'")

                # Making the remote procedure call
                response = stub.Unary(request_message, timeout=15)

                # Print response from server
                self.stdout.write(self.style.SUCCESS(f"grpc response received successfully"))
                self.stdout.write(self.style.SUCCESS(f"Server responded: '{response.text}'"))

        except grpc.RpcError as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: '{e}'"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An unexpected error occurred: '{e}'"))
        finally:
            self.stdout.write("grpc request process finished")