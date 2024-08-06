from simple_image_download import simple_image_download as simp

response = simp.simple_image_download
keywords = ["Indian Currency papernote","Indian Ten Rupees Papernote", "Indian 20 Rupees Papernote", "Indian 50 Rupees Papernote", "Indian 100 Rupees Papernote", "Indian 500 Rupees Papernote", "Indian 2000 Rupees Papernote"]
for kw in keywords:
    response().download(kw, 30)