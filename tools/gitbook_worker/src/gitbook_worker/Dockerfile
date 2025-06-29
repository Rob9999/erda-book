FROM pandoc/latex:latest

# install fonts
RUN apk add --no-cache font-dejavu
RUN mkdir -p /usr/share/fonts
RUN wget -O /usr/share/fonts/OpenMoji-black-glyf.ttf https://github.com/hfg-gmuend/openmoji/raw/master/font/OpenMoji-black-glyf/OpenMoji-black-glyf.ttf && \
    fc-cache -f -v
RUN fc-cache -f -v

# Update TeXLive und installiere pdflscape
RUN tlmgr update --self --all && tlmgr install pdflscape

WORKDIR /data