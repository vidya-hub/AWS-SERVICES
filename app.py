import boto3
from cv2 import cv2
from PIL import Image

def resizeimage(img):
    scale_percent = 50  
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized

def detect_faces_from_s3(photo):
    rek = boto3.client('rekognition', region_name='us-east-1')
    image_dict = {'S3Object':{'Bucket': 'storage-aws-recognition', 'Name':'sample.jpg'}}
    faces = rek.detect_faces(Image=image_dict)
    return faces
def detect_faces_from_localfile(photo):
    client=boto3.client('rekognition')
    with open(photo, 'rb') as image:
        response = client.detect_faces(Image={'Bytes': image.read()})
    return response

def main():
    photo='sample.jpg'
    faceslist=[]
    image = Image.open(open(photo,'rb'))
    iwidth,iheight=image.size
    res=detect_faces_from_localfile(photo)
    
    faces=res["FaceDetails"]
    for face in faces:
        faceslist.append(face)

    # lan=face_1["Landmarks"]
    while True:
        image=cv2.imread(photo)
        # cv2.circle(image,(round(lan[0]["X"]*iwidth),
            # round(lan[0]["Y"]*iheight)),5,(0,0,255),-1)
        for face in faceslist:
            left = iwidth * face["BoundingBox"]['Left']
            top = iheight * face["BoundingBox"]['Top']
            width = iwidth * face["BoundingBox"]['Width']
            height = iheight * face["BoundingBox"]['Height']
            cv2.rectangle(image, (round(left),round(top)),
                      (round(left+width),round(top+height)), (0, 255, 0), 2)
        image=resizeimage(image)
        cv2.imshow("image",image)
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



