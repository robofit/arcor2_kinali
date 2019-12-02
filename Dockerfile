FROM arcor2_base:0.1.0

COPY . /root/arcor2_kinali

RUN cd ~/arcor2_kinali/ \
	&& pip install -e .

RUN ln -fs /root/arcor2_kinali/docker/start.sh /start.sh
