from Project.filter import butter_low_pass
from Project.show_plot import show
from Project import filtfilt, np
# from scipy.signal import  filtfilt


def main():
    order = 6  # 滤波器阶数
    fs = 400.0  # 采样率 hz
    freq_cut = 15  # 截止频率
    b, a = butter_low_pass(freq_cut, fs, order)
    # b, a = butter_band([10, 100], fs, order)
    pwd = "../data/"
    file = "butterfly1.csv"
    data_x = np.loadtxt(pwd + file, delimiter=',', usecols=(6,), skiprows=1)
    data_y = np.loadtxt(pwd + file, delimiter=',', usecols=(7,), skiprows=1)
    data_z = np.loadtxt(pwd + file, delimiter=',', usecols=(8,), skiprows=1)
    data = [data_x, data_y, data_z]
    # y = lfilter(b, a, data)  # 有偏移量
    y = [filtfilt(b, a, data_x), filtfilt(b, a, data_y), filtfilt(b, a, data_z)]  # 无偏移量
    show(y, freq_cut, order)


if __name__ == '__main__':
    main()

