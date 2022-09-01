FROM python:3.7-bullseye

# Add the external tasks directory into /app
ADD app /app

# Install the required dependencies via pip
RUN wget https://github.com/edenhill/librdkafka/archive/v1.9.0.tar.gz && tar xvzf v1.9.0.tar.gz && cd librdkafka-1.9.0/ && ./configure && make && make install && ldconfig
RUN pip install -r /app/requirements.txt

# Expose the required Locust ports
EXPOSE 5557 5558 8089

# Set script to be executable
RUN chmod 755 /app/run.sh

# Start Locust using LOCUS_OPTS environment variable
ENTRYPOINT ["/app/run.sh"]