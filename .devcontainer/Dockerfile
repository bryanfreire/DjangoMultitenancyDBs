FROM python

ARG USER=bfreire
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID $USER \
    && useradd -m -u $UID -g $GID $USER \
    && mkdir /workspace \
    && chown $UID:$GID -R /workspace

WORKDIR /workspace

USER $USER
