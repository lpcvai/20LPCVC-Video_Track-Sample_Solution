#!python3

import json
import math

import cv2
import numpy as np
import torch
import os
torch.backends.quantized.engine = 'qnnpack'

class OCRLib:
    def __init__(self, config_file, det_model_path=None, ocr_model_path=None):
        with open(config_file, "r") as h_config:
            self.config = json.load(h_config)

        dirname = os.path.dirname(config_file)

        if det_model_path is None:
            det_model_path = self.config["det_model"]
            det_model_path = os.path.join(dirname, det_model_path)
        if ocr_model_path is None:
            ocr_model_path = self.config["ocr_model"]
            ocr_model_path = os.path.join(dirname, ocr_model_path)

        self.detector = OCRLib.Detection(
            model_path=det_model_path,
            detection_size=self.config["detection_size"],
            rotated_box=self.config["rotated_box"],
        )

        self.recognizer = OCRLib.Recognition(
            model_path=ocr_model_path,
            image_height=self.config["image_height"],
            hs_factor=self.config["hs_factor"],
            charset=self.config["charset"],
        )

    def process_rgb_image(self, input_image):
        boxes, scores = self.detector.detect(input_image)

        results = []
        for box, score in zip(boxes, scores):
            result = self.recognizer.recognize(input_image, box)
            result["box"] = box.tolist()
            result["det_scr"] = score
            results.append(result)

        return results

    class Detection:
        def __init__(self, model_path, detection_size, rotated_box):
            self.model = torch.jit.load(model_path)
            self.detection_size = detection_size
            self.rotated_box = rotated_box

        def convert_horizontal_boxes(self, boxes, scale):
            ret_data = []
            boxes = boxes / scale
            for [x1, y1, x2, y2] in boxes.tolist():
                ret_data.append([(x1, y1), (x2, y1), (x2, y2), (x1, y2)])
            return ret_data

        def convert_rotated_boxes(self, boxes, scale):
            ret_data = []
            boxes[:, 0:4] = boxes[:, 0:4] / scale
            x_vecs = np.array([-1, 1, 1, -1]) * 0.5
            y_vecs = np.array([-1, -1, 1, 1]) * 0.5
            w_padding = 10
            h_padding = 10
            for cnt_x, cnt_y, w, h, angle in boxes.tolist():
                theta = angle * math.pi / 180.0
                c, s = math.cos(theta), math.sin(theta)
                w = w + w_padding
                h = h + h_padding
                # Rotate boxes
                box_x = cnt_x + (s * y_vecs * h + c * x_vecs * w)
                box_y = cnt_y + (c * y_vecs * h - s * x_vecs * w)
                ret_data.append(np.stack([box_x, box_y], axis=-1))
            return ret_data

        def prepare_inputs(self, input_image):
            scale_ratio = float(self.detection_size) / min(input_image.shape[0:2])
            height = int(input_image.shape[0] * scale_ratio)
            width = int(input_image.shape[1] * scale_ratio)
            im = cv2.resize(input_image, (width, height))

            return (
                torch.from_numpy(im).float().permute(2, 0, 1).unsqueeze(0),
                torch.tensor([[height, width, scale_ratio]]),
            )

        def detect(self, input_image):
            inputs = self.prepare_inputs(input_image)
            boxes, scores, _ = self.model(inputs)

            scale = inputs[1][0][2]
            if self.rotated_box:
                boxes = self.convert_rotated_boxes(boxes, scale)
            else:
                boxes = self.convert_horizontal_boxes(boxes, scale)

            return boxes, scores.tolist()

    class Recognition:
        def __init__(self, model_path, image_height, hs_factor, charset=None):
            self.rcg_module = torch.jit.load(model_path)
            self.image_height = image_height
            self.hs_factor = hs_factor
            self.charset = charset

        def prepare_inputs(self, input_image, box):
            # Find homography transform and apply
            b_w = np.linalg.norm(box[0] - box[1])
            b_h = np.linalg.norm(box[1] - box[2])
            t_h = self.image_height
            t_w = math.floor(b_w * t_h / b_h * self.hs_factor)
            trgt_box = np.array(
                [[0, 0], [t_w, 0], [t_w, t_h], [0, t_h]], dtype="float32"
            )

            # Apply transform
            xfm_mat = cv2.getPerspectiveTransform(
                np.array(box, dtype="float32"), trgt_box
            )
            text_patch = cv2.warpPerspective(input_image, xfm_mat, (t_w, t_h))
            return (
                torch.from_numpy(text_patch).float().permute(2, 0, 1).unsqueeze(0)
                / 255.0
            )

        def recognize(self, input_image, box):
            # Setup inputs
            inputs = self.prepare_inputs(input_image, box)
            symbols, score = self.rcg_module(inputs)

            symbols = symbols.tolist()
            score = score.item()
            decode_str = "".join([self.charset[int(x)] for x in symbols])

            return {
                "rcg_val": symbols,
                "rcg_len": len(symbols),
                "rcg_str": decode_str,
                "rcg_scr": score,
            }
