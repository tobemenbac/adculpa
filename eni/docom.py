core_v1_api = client.CoreV1Api()
body = client.V1Service(
    api_version="v1",
    kind="Service",
    metadata=client.V1ObjectMeta(
        name="service-example"
    ),
    spec=client.V1ServiceSpec(
        selector={"app": "deployment"},
        ports=[client.V1ServicePort(
            port=5678,
            target_port=5678
        )]
    )
)
core_v1_api.create_namespaced_service(namespace="default", body=body)
