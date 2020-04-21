Overview

This baseline OCR solution is a two step solution involving: 1) a text detection step, and 2) a text recognition step. The detection step (1), finds arbitrary rotated bounding boxes of text within a given image. It uses a Faster-RCNN detection architecture with a rotation RPN [1]. The trunk is based on the dmasking model from the FBNet family for efficiency [2]. The recognition step (2) is run on image patches cropped from the original image to recognize single words from the bounding box. It is based on the character sequence encoding (CHAR) as proposed in [3]. The trunk is based on the fbnet_c model from the FBNet family for efficiency [2].

The models were trained with publicly available datasets. For the text detection mode, we use the SynthText in the Wild dataset [4]. The model was trained with detectron2go framework [5]. For the text recognition model, we use data from both [4] and [6] for training. 

[1] J. Ma, W. Shao, H. Ye, L. Wang, H. Wang, Y. Zheng, and X. Xue. "Arbitrary-oriented scene text detection via rotation proposals",  in IEEE Trans. on Multimedia, 2018

[2] B. Wu, X. Dai, P. Zhang, Y. Wang, F. Sun, Y. Wu, Y. Tian, P. Vajda, Y. Jia, and K. Keutzer, “FBNet: Hardware-Aware Efficient ConvNet Design via Differentiable Neural Architecture Search”, in CVPR, 2019

[3] M. Jaderberg, K. Simonyan, A. Vedaldi, and A. Zisserman. “Synthetic Data and Artificial Neural Networks for Natural Scene Text Recognition”, in NeurIPS Deep Learning Workshop, 2014

[4] A. Gupta, A. Vedaldi, and A. Zisserman, “Synthetic Data for Text Localisation in Natural Images”, in CVPR, 2016

[5] https://github.com/facebookresearch/mobile-vision/tree/master/detectron2go

[6] M. Jaderberg, K. Simonyan, A. Vedaldi, and A. Zisserman, “Reading Text in the Wild with Convolutional Neural Networks”, in IJCV, 2016



How to run

python ./query_video.py --input_video <video file> --query_file <query text file> --config_file ./config.json

