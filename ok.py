import torch
import sys

if __name__ == '__main__':
    # train()
    print(torch.cuda.is_available())
    print(sys.path)
    sys.path.append('./result_gpu/attunet/model/model_obj.pth')
    print(sys.path)
