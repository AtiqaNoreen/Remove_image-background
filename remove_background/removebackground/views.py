from django.shortcuts import render
from django.conf import settings
from rembg import remove
from PIL import Image
import os

def remove_bg_view(request):
    output_url = None

    if request.method == "POST":
        image_name = request.POST.get("image_name")
        
        # static se image uthao
        input_path = os.path.join(settings.BASE_DIR, "removebackground", "static", image_name)

        output_name = "output.png"
        output_path = os.path.join(settings.BASE_DIR, "removebackground", "static", output_name)

        # open image
        input_image = Image.open(input_path)
        output_image = remove(input_image)

        if output_path.lower().endswith(".jpg") or output_path.lower().endswith(".jpeg"):
            output_image = output_image.convert("RGB")

        output_image.save(output_path)

        # static url banake bhejo
        output_url = settings.STATIC_URL + output_name

    return render(request, "index.html", {"output_image_url": output_url})
