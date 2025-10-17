import azure.functions as func
from azure.cosmos import CosmosClient
import os
import json

# Create FunctionApp instance
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Define route for your API
@app.route(route="GetRecommendations", methods=["POST"])
def get_recommendations(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Parse moods from request
        req_body = req.get_json()
        moods = req_body.get("moods", [])

        if not moods:
            return func.HttpResponse(
                json.dumps({"error": "Please provide at least one mood."}),
                mimetype="application/json",
                status_code=400
            )

        # Load Cosmos DB credentials
        endpoint = os.environ["COSMOS_ENDPOINT"]
        key = os.environ["COSMOS_KEY"]
        database_name = os.environ["COSMOS_DATABASE"]
        container_name = os.environ["COSMOS_CONTAINER"]

        # Connect to Cosmos DB
        client = CosmosClient(endpoint, credential=key)
        container = client.get_database_client(database_name).get_container_client(container_name)

        # Query: find songs matching selected moods
        query = "SELECT * FROM c WHERE ARRAY_CONTAINS(@moods, c.mood, true)"
        parameters = [{"name": "@moods", "value": moods}]
        items = list(container.query_items(
            query=query,
            parameters=parameters,
            enable_cross_partition_query=True
        ))

        # Return JSON result
        return func.HttpResponse(
            json.dumps({"recommendations": items}),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=500
        )
