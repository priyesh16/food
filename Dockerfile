FROM centos:7

RUN yum install git cmake -y
RUN yum groupinstall 'Development Tools' -y

RUN yum install gcc-c++ \
    libXi-devel openexr-devel SDL-devel fftw-devel libtiff-devel \
    freetype-devel libogg-devel libjpeg-devel openjpeg openjpeg-devel \
    libpng-devel vim libGLU-devel libffi-devel zlib-devel bzip2-devel \
	openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel \
	gdbm-devel db4-devel libpcap-devel xz-devel  wget -y

# Install Python3.6
ENV LD_LIBRARY_PATH /usr/local/lib:/usr/local/lib64
RUN cd ~ && \
    wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz && \
    tar xzf Python-3.6.6.tgz && \
    cd Python-3.6.6 && \
    ./configure --enable-shared --with-openssl='/usr/include/openssl' && \
    make install && \
    ldconfig && python3 --version

RUN yum install epel-release -y
RUN yum install blender -y

COPY requirements.txt /bld/
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /bld/requirements.txt
