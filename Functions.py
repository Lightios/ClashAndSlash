import pygame as pg


def rot_image_around_center(image, angle, x, y):
    """
    Rotates sprite's image by it's current angle
    :param image: sprite's image
    :param angle: sprite's angle
    :param x: sprite's position x
    :param y: sprite's position y
    :returns: image and rect
    """
    rotated_image = pg.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)

    return rotated_image, new_rect

