from PIL import Image                           # May need: pip3 install Pillow
from facenet_pytorch import InceptionResnetV1   # May need: pip3 install facenet_pytorch
from torchvision import datasets, transforms    # May need: pip3 install torch torchvision
import torch
import numpy as np                              # May need: pip3 install numpy
import argparse

def remove_transparency(im):
    n = np.array(im)
    n = n[:, :, :3]
    return Image.fromarray(n)

# Loads an image, resizes it, removes transparency, and converts to a tensor
def load_image_to_tensor(img_fn, size=(160,160)):
    img = Image.open(img_fn)
    return transforms.ToTensor()(remove_transparency(img.resize(size)))

def save_tensor_to_image(tensor, img_fn):
    im = transforms.ToPILImage()(tensor)
    im.save(img_fn)

def main():
    parser = argparse.ArgumentParser(description="Adversarial faces")
    parser.add_argument('--image', type=str, default=None, help='Image to start from')
    parser.add_argument('--goal', type=str, default=None, help='Goal image to head toward')
    parser.add_argument('--out', type=str, default='adv.png', help='Output image filename')
    parser.add_argument('--threshold', type=float, default=0.75, help='Keep going until we are threshold distance from goal')
    parser.add_argument('--lr', type=float, default=0.1, help='Learning rate')

    args = parser.parse_args()

    # Load Inception resnet model, trained with VGGFace2
    resnet = InceptionResnetV1(pretrained='vggface2').eval()

    # Load images
    goal_tensor = load_image_to_tensor(args.goal)
    img_tensor  = load_image_to_tensor(args.image)

    img_tensor = img_tensor.clone()
    img_tensor = img_tensor.detach()
    img_tensor = img_tensor.requires_grad_(True)

    # Compute embedding from target
    goal_embedding = resnet(goal_tensor.unsqueeze(0))

    for i in range(250):
        image_embedding = resnet(img_tensor.unsqueeze(0))
        loss = torch.dist(image_embedding, goal_embedding)
        loss.backward(retain_graph=True)
        img_tensor.data -= img_tensor.grad.data * args.lr 
        img_tensor.data = torch.clamp(img_tensor.data, 0, 1)
        img_tensor.grad.data.zero_()
        print("Current Loss:", loss.item())
    
        if loss.item() < args.threshold:
            save_tensor_to_image(img_tensor, args.out)
            return
        
    # TODO: perform your adversarial example here
    # Modify img_tensor until its embedding (resnet(img_tensor.unsqueeze(0)))
    #   is similar to goal_embedding
    # (e.g. torch.cdist(img_embedding, goal_embedding) < args.threshold)
    #
    # Output the resulting image to args.out
    #   (e.g. save_tensor_to_image(img_tensor, args.out))

if __name__=='__main__':
    main()
