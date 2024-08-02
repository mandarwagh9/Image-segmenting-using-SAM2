import os
import replicate

# Set the REPLICATE_API_TOKEN environment variable
os.environ['REPLICATE_API_TOKEN'] = 'your_replicate_api_token_here'

# Check if the token is set correctly
if 'REPLICATE_API_TOKEN' not in os.environ:
    raise ValueError("API token not found. Set the REPLICATE_API_TOKEN environment variable.")

# URL of the uploaded image (replace with your actual URL)
image_url = "https://i.imgur.com/your_uploaded_image.jpg"  # Example Imgur URL

# Define the input parameters for the model
input = {
    "image": image_url,
    "use_m2m": True,
    "points_per_side": 32,
    "pred_iou_thresh": 0.88,
    "stability_score_thresh": 0.95
}

# Run the model
output = replicate.run(
    "meta/sam-2:fe97b453a6455861e3bac769b441ca1f1086110da7466dbb65cf1eecfd60dc83",
    input=input
)

print(output)
