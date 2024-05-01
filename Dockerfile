FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install rdkit-pypi==2022.9.5
RUN pip install protobuf==3.18.3
RUN pip install tensorboardx==2.0
RUN pip install chemprop==1.5.2
RUN pip install tensorboard==2.11.0

# Clone the repository
RUN git clone --branch v4.3.5 --single-branch https://github.com/MolecularAI/REINVENT4

# Install the package using pip
RUN pip install -r ./REINVENT4/requirements-linux-64.lock
RUN pip install --no-deps ./REINVENT4

WORKDIR /repo
COPY . /repo