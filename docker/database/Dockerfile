FROM mongo:bionic

RUN apt-get update \
	&& apt-get install -y git python3-pip

## Add deploy keys
RUN mkdir -p /root/.ssh/
RUN mkdir -p /etc/ssh
ADD deploy_keys/robofit_arcor2_deploy /
ADD ssh_config /
RUN chmod 600 /robofit_arcor2_deploy \
	&& echo "StrictHostKeyChecking no" > /etc/ssh/ssh_config \
    && cat /ssh_config >> /etc/ssh/ssh_config

RUN cd ~ \
	&& git clone git@arcor2.github.com:robofit/arcor2.git

RUN cd ~/arcor2 \
	&& pip3 install -e .

RUN cd \
	&& git clone https://github.com/s-knibbs/dataclasses-jsonschema.git \
	&& cd dataclasses-jsonschema \
	&& pip3 install -e .

RUN pip3 install --upgrade setuptools PyYAML

ADD start.sh /

ENV PYTHONPATH ~

expose 5001