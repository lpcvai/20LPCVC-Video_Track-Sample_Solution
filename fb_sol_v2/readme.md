### This solution is formatted to from the **[Facebook Baseline Solution](https://github.com/sstsai-adl/workshops/tree/master/LPCV_2020/uav_video_challenge)**

#### Differences Between V1 and V2
This solution uses a quantized recognition model that has better runtime than the previous solution. The detection model was quantized using post training quantization. For the recognition model, Facebook used quantization aware training. Default quantization configurations were used with qnnpack engines.

This solution also adds support for the AArch64 architecture, which gives access to the Raspberry Pi FPU. The plain armv7l wheel provided previously does not take advantage of the FPU and uses software floating point emulation. Using the FPU speeds up the model and decreases energy consumption.
