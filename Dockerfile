# docker build --tag registry.yuedaowang.com/ydx_combo_api:0.1.0 .

FROM python:3

ENV HOME /root
ENV SRC interface

WORKDIR $HOME/$SRC

# Copy source code to docker if no git server
COPY . $HOME/$SRC

RUN pip install -r requirements.txt
