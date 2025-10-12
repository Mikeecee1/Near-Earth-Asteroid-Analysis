# Technical Info (detailed)

This report lists the exact import lines found in the project's notebooks and a short note where each library is used. You can copy these lines to remove or refactor imports inside each notebook.

Files scanned:
- jupyter_notebooks/ETL.ipynb
- jupyter_notebooks/Visualisation.ipynb
- jupyter_notebooks/Modelling.ipynb
- jupyter_notebooks/ML_Modelling.ipynb

---

## Exact import lines (grouped by notebook)

### ETL.ipynb

```python
%matplotlib inline
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

# used for data profiling (optional)
from ydata_profiling import ProfileReport
```

Notes: `os` is used for working-directory checks; `ydata_profiling` produces a profiling HTML report (requires additional packages such as `ipywidgets` when rendering interactively).

---

### Visualisation.ipynb

```python
%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import sklearn as sklearn
import warnings
warnings.filterwarnings('ignore')
sns.set_style(style="whitegrid")

# Statistical helper
import pingouin as pg

# SciPy statistical routines used (examples from notebook)
from scipy.stats import mannwhitneyu
from scipy.stats import spearmanr
from scipy.stats import ttest_ind
```

Notes: `sklearn` is imported at the top level in this notebook but not referenced via that namespace in the EDA cells — specific sklearn functions are used in the modelling notebooks rather than here.

---

### Modelling.ipynb

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# import plotly.graph_objects as go  # commented in the notebook
from scipy import stats
from sklearn.preprocessing import KBinsDiscretizer
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
```

Notes: main purpose is data remodelling, binning and visual checks. `KBinsDiscretizer` is present though binning in the notebook uses `pd.cut` in many places.

---

### ML_Modelling.ipynb

Top-level / plotting imports:
```python
# display / plotting
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
```

Modelling / pipeline imports (used later in notebook):
```python
from sklearn.pipeline import Pipeline
from feature_engine.imputation import MeanMedianImputer, CategoricalImputer
from feature_engine.encoding import OrdinalEncoder
from sklearn.feature_selection import SelectFromModel

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.metrics import (
    accuracy_score, roc_auc_score, average_precision_score,
    classification_report, confusion_matrix, ConfusionMatrixDisplay
)
```

Notes: `feature_engine` is used for imputation and ordinal encoding inside pipelines. GridSearchCV and StratifiedKFold are used to tune models (refit on recall in the notebook).

---

## Imports that appear unused or redundant (recommend reviewing/removing)
- `import sklearn as sklearn` in `Visualisation.ipynb` — top-level import not used directly in that notebook.
- `plotly.graph_objects as go` is imported in ML_Modelling but not always used in visible cells — check whether it is needed or can be removed.
- Both `from scipy import stats` and `from scipy.stats import <func>` are present across notebooks; prefer using one style to avoid redundancy.

---

---

