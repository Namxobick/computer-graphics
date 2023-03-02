from filters_opencv.filters.local_filters.utils.constants import SHARRA_KERNEL_X, SHARRA_KERNEL_Y
from filters_opencv.filters.local_filters.utils.methods.image_changes import apply_kernels
from filters_opencv.image import Image


def sharra(image: Image):
    apply_kernels(image, [SHARRA_KERNEL_X, SHARRA_KERNEL_Y])
