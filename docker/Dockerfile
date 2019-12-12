FROM arcor2/arcor2_base:0.1.1

COPY . /root/arcor2_kinali

RUN cd ~/arcor2_kinali/ \
	&& pip install -e .

RUN ln -fs /root/arcor2_kinali/docker/start.sh /start.sh

EXPOSE 6789
