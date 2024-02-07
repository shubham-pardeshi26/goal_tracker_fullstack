import requests
import json

token = "9dfcd4a1-2768-43f2-b079-2d7f6aeb8a18"
# URL of the Jupyter Notebook server
jupyter_url = "http://localhost:8888"  # Adjust as needed

# Headers for the request
headers = {
    "Authorization": f"token {token}",  # Replace with your Jupyter token
    "Content-Type": "application/json",
}

# Data for creating a new notebook
data = json.dumps(
    {
        "type": "notebook",
        "content": {
            "metadata": {
                "kernelspec": {
                    "name": "python3",
                    "display_name": "Python 3",
                    "language": "python",
                }
            },
            "nbformat": 4,
            "nbformat_minor": 4,
            "cells": [],
        },
    }
)

# Endpoint for creating files
api_endpoint = f"{jupyter_url}/api/contents/work/new-notebook.ipynb"

# Make the API request
response = requests.put(api_endpoint, headers=headers, data=data)

# Check the response
if response.status_code == 201:
    print("Notebook created successfully.")
else:
    print(f"Failed to create notebook. Status code: {response.status_code}")
