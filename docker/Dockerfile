ARG version=latest
FROM arcor2/arcor2_base:$version

COPY . /root/arcor2_kinali

RUN cd ~/arcor2_kinali/ \
	&& pip install -e .

EXPOSE 6789
