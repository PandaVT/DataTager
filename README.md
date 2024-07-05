# DataTager
Fine-Tune LLM Synthetic-Data application and "From Data to AGI: Unlocking the Secrets of Large Language Model"

![](https://raw.githubusercontent.com/PandaVT/DataTager/main/assert/DataTager_paper_Framework.png)

## Installation

To install the necessary dependencies, follow the steps below:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/PandaVT/DataTager.git
cd DataTager
```

2. Create and activate a Conda environment using the provided YAML file:

```
conda env create -f config/env.yaml && conda clean -afy
conda activate DataTager
```

3. Install additional dependencies using pip:

```
conda run --no-capture-output --name DataTager pip install --no-cache-dir openai==1.30.2 retry -i https://pypi.tuna.tsinghua.edu.cn/simple

```

## How to use

1. config the LLM-apikeys in read_pdf.py
2. run scripts below
```
python read_ppt.py
python generate_ppt.py
```

## Contacts

https://x.com/data_tager

https://discord.gg/GCY2Ph8Fdk

![](https://raw.githubusercontent.com/PandaVT/DataTager/main/assert/wechat_group.jpg)

