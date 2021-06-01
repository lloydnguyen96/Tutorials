# marketplace/marketplace.py
import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
recommendations_client = RecommendationsStub(recommendations_channel)

@app.route("/")
def render_hompage():
    """TODO: Docstring for render_hompage.
    :returns: TODO

    """
    recommendation_request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(
        recommendation_request
    )
    return render_template(
        "homepage.html",
        recommendations=recommendations_response.recommendations,
    )
