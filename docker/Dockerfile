ARG version=latest
FROM arcor2/arcor2_base:$version

COPY . /root/arcor2_kinali

RUN cd ~/arcor2_kinali/ \
	&& pip install -e .

CMD ["python", "/root/arcor2_kinali/arcor2_kinali/object_types/upload.py"] 
