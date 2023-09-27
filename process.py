import pyvips

def read_bytes(buffer: bytes):
    image = pyvips.Image.new_from_buffer(
            data=buffer, options="", fail=True
        ).autorot()
    image.avg() # to force loading image
    return image

def write_bytes_jpeg(image):
    buffer = image.jpegsave_buffer(Q=95, background=(255, 255, 255))
    return buffer

