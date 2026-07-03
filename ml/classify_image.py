import torch
from torchvision import models, transforms
from PIL import Image

# 1. Load pretrained model
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

# 2. Preprocessing transformations
preprocess = models.ResNet18_Weights.DEFAULT.transforms()

# 3. Load and preprocess image
img = Image.open('path/to/image').convert('RGB')
input_tensor = preprocess(img).unsqueeze(0)  # shape: [1, 3, 224, 224]

# 4. Inference
with torch.no_grad():
    logits = model(input_tensor)
    probs = torch.softmax(logits, dim=1)

# 5. Get prediction label
class_id = probs.argmax().item()
print(class_id)
label = models.ResNet18_Weights.DEFAULT.meta['categories'][class_id]

print(label)
