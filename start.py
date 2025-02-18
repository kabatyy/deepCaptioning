import os 
import subprocess

CLONE_DIR = "/content/project"
COCO_API_DIR = os.path.join(CLONE_DIR, "deepCaptioning/cocoapi")

def download_images():
    train_images_url = "http://images.cocodataset.org/zips/train2014.zip"
    val_images_url= "http://images.cocodataset.org/zips/val2014.zip"
    test_images_url= "http://images.cocodataset.org/zips/test2014.zip"
    train_val_annotations_url = "http://images.cocodataset.org/annotations/annotations_trainval2014.zip"
    
    train_zip_path = os.path.join(CLONE_DIR, "train2014.zip")
    val_zip_path = os.path.join(CLONE_DIR, "val2014.zip")
    test_zip_path = os.path.join(CLONE_DIR, "test2014.zip")
    annotations_trainval_zip_path = os.path.join(CLONE_DIR, "annotations_trainval2014.zip")

    subprocess.run(["wget", "-O", train_zip_path, train_images_url], check=True)
    subprocess.run(["wget", "-O", val_zip_path, val_images_url], check=True)
    subprocess.run(["wget", "-O", test_zip_path, test_images_url], check=True)
    subprocess.run(["wget", "-O", annotations_trainval_zip_path,    train_val_annotations_url], check=True)
    print("Downloaded images and annotations")
    return train_zip_path, val_zip_path, test_zip_path, annotations_trainval_zip_path
  

def extract_images(train_zip_path, val_zip_path, test_zip_path, annotations_trainval_zip_path):
    train_extract_dir = os.path.join(COCO_API_DIR, "images/train2014")
    os.makedirs(train_extract_dir, exist_ok=True)
    test_extract_dir =  os.path.join(COCO_API_DIR, "images/test2014")
    os.makedirs(test_extract_dir, exist_ok=True)
    val_extract_dir = os.path.join(COCO_API_DIR, "images/val2014")
    os.makedirs(val_extract_dir, exist_ok=True)
    annotations_extract_dir = os.path.join(COCO_API_DIR, "annotations/annotations")
    os.makedirs(annotations_extract_dir, exist_ok=True)

    subprocess.run(["unzip", "-o",], train_zip_path, "-d", train_extract_dir, check=True)
    subprocess.run(["unzip", "-o",], val_zip_path, "-d", test_extract_dir, check=True)
    subprocess.run(["unzip", "-o",], test_zip_path, "-d", val_extract_dir, check=True)
    subprocess.run(["unzip", "-o",], annotations_trainval_zip_path, "-d", annotations_extract_dir, check=True)
    print(f"Images extracted.")


if __name__ == "__main__":
 
    train_zip_path, val_zip_path, test_zip_path, annotations_trainval_zip_path = download_images()
    extract_images(train_zip_path, val_zip_path, test_zip_path, annotations_trainval_zip_path)
    
