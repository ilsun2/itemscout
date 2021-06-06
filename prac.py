import os
def create_category_folder(categoryName):
    parent_dir = "/Users/ilsunchoi/Documents/itemscout/"
    directory = categoryName
    path = os.path.join(parent_dir, directory)
    os.makedirs(path, exist_ok=True)


def create_product_folder(categoryName,productName):
    parent_dir = f"/Users/ilsunchoi/Documents/itemscout/{categoryName}/"
    directory = productName
    path = os.path.join(parent_dir, directory)
    os.makedirs(path, exist_ok=True)
    return path