print('running main')

# from generators.gen_video import generate_video
# from generators.gen_images import generate_images
# from generators.gen_audio import generate_audio

# from generators import (generate_audio,generate_images,generate_video)


#if you dont want to use init

from generators.audio.gen_audio import *         # * = everything
from generators.video.gen_video import *         # * = everything
from generators.images.gen_images import *         # * = everything


generate_audio()
generate_images()
generate_video()