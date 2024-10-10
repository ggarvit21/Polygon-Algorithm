# Use Ubuntu as the base image
FROM ubuntu:18.04

# Set environment variables to avoid user prompts during installations
ENV DEBIAN_FRONTEND=noninteractive

# Update package repository and install system utilities
RUN apt-get update && apt-get install -y \
    software-properties-common \
    build-essential \
    g++ \
    wget \
    curl \
    git \
    cmake \
    libgmp-dev \
    libmpfr-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python 2, Python 3, and development headers
RUN apt-get update && apt-get install -y \
    python2.7 \
    python2.7-dev \
    python3 \
    python3-dev \
    python3-pip \
    && ln -s /usr/bin/python2.7 /usr/bin/python2 \
    && rm -rf /var/lib/apt/lists/*

# Install pip for Python 2
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && python2 get-pip.py && rm get-pip.py

# Install required Python 2 libraries
RUN pip2 install numpy easygui matplotlib

RUN apt-get update && rm -rf /var/lib/apt/lists/*

# Set up a working directory
WORKDIR /workspace
RUN git clone 
RUN cd 
# Set Python 3 as the default Python version
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# Verify Python versions to ensure all installations are correct
RUN python --version && python2 --version && python3 --version
RUN apt install -y python-tk
RUN  apt install xvfb
RUN Xvfb :99 -screen 0 1920x1080x24 & export DISPLAY=:99
# Command to run by default in the container
CMD ["/bin/bash"]
