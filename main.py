import cv2
from sys import argv

def get_frames(url: str, id: str):
    video = cv2.VideoCapture(url)
    ok, frame = video.read()
    count = 0
    name = 100
    while ok:
        if count % 1 == 0:
            cv2.imwrite(f"output/{id}/frame_{name}.jpg", frame)
            name += 1
            print(f"Frame: {name}")
        count += 1
        ok, frame = video.read()
    video.release()




if __name__ == "__main__":
    get_frames(argv[1], "test2")

