'''
现实任务中通常是利用有限个测试样例来绘制 ROC ，此时仅能获得有
限个(真正例率，假正例 )坐标对，无法产生图 的光滑 ROC 曲线， 只能
绘制出所示的近似 ROC 曲线.绘图过程如下:
给定 m+ 个正例和个反例，根据学习器预测结果对样例进排序，然后把分类阔值设最大，
即把所样例均预测为反例，此时真正例率和假正例率均为 坐标
标记一个点然后，将分类阈值依次设为每个样例的预测值，即依次将每个样例
划分为正例.设前一个标记点坐标为（x，y） ，若为真正例，则对应标记点的
坐标为 (X ，y+(1/m+)) ;当前若为假正例，则对应标记点的坐标为 (X+1/m- ,y) ，
然后用线段连接相邻点即ROC曲线
'''
import matplotlib.pyplot as plt

list = [0.8, 0.9, 0.2, 0.1, 0.4, 0.6, 0.7, 0.3, 0.8, 0.25]
tf_list = [1, 1, 0, 0, 0, 0, 1, 0, 1, 0]
# 给定一个分类器打分的列表，给定真实的正反例，4个正例(1,2,7,9)，6个反例(3,4,5,6,8,10)
# 排序
# thresh=[1]
# thresh1=thresh+list
# print(thresh1)
m_true = 0
m_flase = 0
for i in range(len(tf_list)):
    if tf_list[i] == 1:  # 真正例
        m_true = m_true + 1
    else:
        m_flase = m_flase + 1
print(m_flase, m_true)  # 6,4
x = []
y = []
xi = 0
yi = 0
for i in range(len(list)):
    if tf_list[i] == 0:  # 假正例
        xi = xi + 1 / m_flase
        yi = yi
        x.append(xi)
        y.append(yi)
    else:  # 真正例
        xi = xi
        yi = yi + 1 / m_true
        x.append(xi)
        y.append(yi)
print(x, y)

plt.plot(x, y)

plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC_picture')
plt.show()  ###显示
AUC = 0
for i in range(len(x) - 1):
    AUC = AUC + (x[i + 1] - x[i]) * (y[i] + y[i + 1])
auc = 0.5 * AUC
print(auc)
