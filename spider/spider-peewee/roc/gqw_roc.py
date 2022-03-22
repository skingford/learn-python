from sklearn import metrics
import pylab as plt
import pandas as pd
import numpy as np
from scipy.interpolate import make_interp_spline

r1 = pd.read_csv(
    r"./有无肝纤维化统计数据.csv",
    header=None,
    names=['初级医师诊', '中级医师诊断', '高级医师诊断', 'AI诊断', '病理']
)


# r2 = pd.read_csv(r"C:\Users\Royalwen\Desktop\xgboost.csv", header=None, names=['用户标识', '标签', '预测'])
# r3 = pd.read_csv(r"C:\Users\Royalwen\Desktop\rf.csv", header=None, names=['标签', '预测'])


def ks(y, s1, s2, s3, s4):
    Font = {'size': 18, 'family': 'Times New Roman'}

    fpr1, tpr1, _ = metrics.roc_curve(y, s1)
    fpr2, tpr2, _ = metrics.roc_curve(y, s2)
    fpr3, tpr3, _ = metrics.roc_curve(y, s3)
    fpr4, tpr4, _ = metrics.roc_curve(y, s4)

    roc_auc1 = metrics.auc(fpr1, tpr1)
    roc_auc2 = metrics.auc(fpr2, tpr2)
    roc_auc3 = metrics.auc(fpr3, tpr3)
    roc_auc4 = metrics.auc(fpr4, tpr4)

    # plt.figure(figsize=(20, 20), dpi=100)
    fig = plt.figure(figsize=(6, 6), dpi=100)
    lw = 2

    plt.plot(fpr1, tpr1, color='r', lw=lw, alpha=0.8, label='Junior = %0.3f' % roc_auc1)
    plt.plot(fpr2, tpr2, color='violet', lw=lw, alpha=0.8, label='Intermediate = %0.3f' % roc_auc2)
    plt.plot(fpr3, tpr3, color="blue", lw=lw, alpha=0.8, label='Senior = %0.3f' % roc_auc3)
    plt.plot(fpr4, tpr4, color="lightgreen", lw=lw, alpha=0.8, label='AI = %0.3f' % roc_auc4)

    plt.legend(loc='lower right', prop=Font, frameon=False)
    plt.plot([0, 1], [0, 1], '--', color='grey')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('Sensitivity', Font)
    plt.xlabel('Specificity', Font)
    # plt.title('ROC Curve', fontsize=25)

    # plt.xticks(np.arange(0, 1, step=0.1))
    # plt.yticks(np.arange(0, 1, step=0.1))

    plt.tick_params(labelsize=15)
    plt.show()
    fig.savefig('gqw_roc.png', dpi=120, bbox_inches='tight')
    return abs(fpr1 - tpr1).max(), abs(fpr2 - tpr2).max(), abs(fpr3 - tpr3).max()


yb = r1.病理[1:220]
score1 = r1.初级医师诊[1:220]
score2 = r1.中级医师诊断[1:220]
score3 = r1.高级医师诊断[1:220]
score4 = r1.AI诊断[1:220]

yb = list(map(int, yb))
score1 = list(map(int, score1))
score2 = list(map(int, score2))
score3 = list(map(int, score3))
score4 = list(map(int, score4))

print(ks(np.array(yb), np.array(score1), np.array(score2), np.array(score3), np.array(score4)))
