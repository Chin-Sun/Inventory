import argparse
import logging
from servicefoundry import Service, Build, PythonBuild, Resources, Port, AppProtocol

logging.basicConfig(level=logging.INFO, format=logging.BASIC_FORMAT)
parser = argparse.ArgumentParser()
parser.add_argument("--workspace_fqn", type=str, required=True,
                    help="FQN of the workspace to deploy to")
args = parser.parse_args()

service = Service(
    name="Inventory",
    image=Build(
        build_spec=PythonBuild(
            python_version="3.8",
            requirements_path="requirements.txt",
            command="python Inventory_server.py"
        )
    ),
    resources=Resources(
        cpu_request=0.2,
        cpu_limit=0.5,
        memory_request=500,
        memory_limit=500,
    ),
    ports=[
        Port(
            port=50052,
            app_protocol=AppProtocol.grpc,
            host="qian.truefoundry.cloud"
            # Note: Your cluster should allow subdomain based routing (*.yoursite.com) for gRPC to work correctly via public internet.
            # A host matching the wildcard base domain for the cluster can be explicitly configured by passing in `host`
        ),
    ],
)

service.deploy(workspace_fqn=args.workspace_fqn)
