import numpy as np
from sklearn.metrics import roc_curve, auc

y = np.array([0, 0, 1, 1])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, _ = roc_curve(y, scores)
roc_auc = auc(fpr, tpr)

y1 = np.array([0, 0, 0, 1])
scores1 = np.array([0.2, 0.3, 0.35, 0.3])
fpr1, tpr1, _ = roc_curve(y1, scores1)
roc_auc1 = auc(fpr1, tpr1)

import matplotlib as mpl
# mpl.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure()
lw = 2

plt.plot(fpr, tpr, color='darkorange', lw=lw, linestyle='-', label='ROC curve (area = %0.2f)' % roc_auc)

plt.plot(fpr1, tpr1, color='red', lw=lw, linestyle='-', label='ROC curve (area = %0.2f)' % roc_auc1)

plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')

plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
# fig.savefig('/tmp/roc.png')
plt.show()
