# https://diagrams.mingrammer.com/

# just run python3 diagram.py

from diagrams import Diagram, Cluster
from diagrams.k8s.compute import Pod
from diagrams.onprem.client import Client
from diagrams.aws.database import Database


with Diagram("kubectl SSH Jump plugin", show=False):

    with Cluster("Your local machine"):
        first_client = Client("first ssh-agent")
        second_client = Client("second ssh-agent")
        third_client = Client("third ssh-agent")

    with Cluster("Internal Network A"):
        with Cluster("Kubernetes Cluster"):
            first_pod = Pod("SSH Jump\ntemporary pod")
            second_pod = Pod("SSH Jump\ntemporary pod")
            third_pod = Pod("SSH Jump\ntemporary pod")
            first_client >> first_pod
            second_client >> second_pod
            third_client >> third_pod
    
    with Cluster("Internal Network B"):
        database = Database("Database")
        another_database = Database("Another Database")
        first_pod >> database
        second_pod >> another_database
        third_pod >> another_database
