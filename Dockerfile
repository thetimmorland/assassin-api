FROM python:3.10 as base
WORKDIR /workdir

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir poetry==1.2.2

COPY pyproject.toml poetry.lock ./
RUN poetry --no-interaction --no-ansi install

COPY . ./

RUN ./scripts/check
RUN poetry build

#
# OUTPUT STAGE
#

FROM python:3.10

RUN --mount=from=base,source=/workdir/dist,target=/mnt/dist \
    pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir mnt/dist/app-*-py3-none-any.whl
