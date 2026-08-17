import base64
import os
img_path = "iso.png"
with open(img_path, "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")


d = f'<img class="iso-seal" src="data:image/jpeg;base64,{b64}" alt="ISO 13485:2016 Medical Devices Quality Management Certified" />'
print(d)