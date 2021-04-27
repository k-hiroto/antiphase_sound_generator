#LRで同じ出力のwav ファイルと逆位相の出力のwav ファイルを同時に作成するプログラム


import soundfile as sf
from scipy.signal import chirp
import numpy as np
import matplotlib.pyplot as plt

# 数値をminus→逆位相にする関数
def calc_minus(n):
    return n * (-1)

# サンプル波形を生成（チャープ信号）
samplerate = 44100                                      # サンプリングレート
ts = 0                                                  # 信号の開始時間
tf = 3                                                # 信号の終了時間
t = np.linspace(ts, tf, tf * samplerate)                # 時間軸を作成
L = chirp(t, f0=100, f1=300, t1=tf, method='linear')    # 100Hz - 300Hz  linear に　tf秒で出力する
R = list(map(calc_minus, L)) #逆位相のリストを作成する

LR_minus =[]
LR_plus =[]

for (L_data, R_data) in zip(L, R):
    LR_minus.append([L_data,R_data])
    LR_plus.append([L_data,L_data])

#[[L,R],[L,R],[L,R] ・・・]　というリストを soundfile はwav に変換することができる

sf.write('stereo_minus.wav', LR_minus, samplerate)
sf.write('stereo_plus.wav', LR_plus, samplerate)